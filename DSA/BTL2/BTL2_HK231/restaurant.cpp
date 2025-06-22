#include "main.h"

//heap
// Heap class
//so sánh min heap
struct MinHeapComparator {
    template<typename T>
    static bool prior(const T& a, const T& b) {
        return a < b;
    }
};
//hàm swap 2 giá trị
template <typename T>
void swap(T* arr, int i, int j) {
    T temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
template <typename E, typename Comp> 
class heap {
protected:
	E* Heap; // Pointer to the heap array
	int maxsize; // Maximum size of the heap
	int n; // Number of elements now in the heap
	queue<int> q;//Lưu thứ tự vào heap trước của các node
	vector<int> v;//lưu thứ tự sử dụng của node
// Helper function to put element in its correct place
	void siftdown(int pos) {
		while (!isLeaf(pos)) { // Stop if pos is a leaf
			int j = leftchild(pos); int rc = rightchild(pos);
			if ((rc < n) && Comp::prior(Heap[rc], Heap[j]))
			j = rc; // Set j to smaller	 child’s value
			if (Comp::prior(Heap[pos], Heap[j])) return; // Done
			swap(Heap, pos, j);
			pos = j; // Move down
		}
	}
public:
	heap(E* h, int num, int max) // Constructor
	{ Heap = h; n = num; maxsize = max; buildHeap(); }
	int size() const // Return current heap size
	{ return n; }
	bool isLeaf(int pos) const // True if pos is a leaf	
	{ return (pos >= n/2) && (pos < n); }
	int leftchild(int pos) const
	{ return 2*pos + 1; } // Return leftchild position
	int rightchild(int pos) const
	{ return 2*pos + 2; } // Return rightchild position
	int parent(int pos) const // Return parent position
	{ return (pos-1)/2; }
	void buildHeap() // Heapify contents of Heap
	{ for (int i=n/2-1; i>=0; i--) siftdown(i); }
	int plusSize(){return n++;}//tăng size 
	// Insert "it" into the heap
	void insert(const E& it) {
		int curr = n++;
		Heap[curr] = it; // Start at end of heap
		// Now sift up until curr’s parent < curr
		while ((curr!=0) && (Comp::prior(Heap[curr], Heap[parent(curr)]))) {
			swap(Heap, curr, parent(curr));
			curr = parent(curr);
		}
	}
	// Remove first value
	E removefirst() {
		swap(Heap, 0, --n); // Swap first with last value
		if (n != 0) siftdown(0); // Siftdown new root val
		return Heap[n]; // Return deleted value
	}
	// Remove and return element at specified position
	E remove(int pos) {
		if (pos == (n-1)) n--; // Last element, no work to do
		else
		{
			swap(Heap, pos, --n); // Swap with last value
			while ((pos != 0) &&
			(Comp::prior(Heap[pos], Heap[parent(pos)]))) {
				swap(Heap, pos, parent(pos)); // Push up large key
				pos = parent(pos);
			}
			if (n != 0) siftdown(pos); // Push down small key
		}
		return Heap[n];
	}

};
//cây huffman
template <typename E> 
class HuffNode {
private:
	int prior;
public:
	virtual ~HuffNode() {} // Base destructor
	virtual int weight() = 0; // Return frequency
	virtual bool isLeaf() = 0; // Determine type
	virtual HuffNode<E> *left() const = 0;
	virtual HuffNode<E> *right() const = 0;
	virtual void setLeft(HuffNode<E>* node) = 0;
	virtual void setRight(HuffNode<E>* node) = 0;
	virtual void setWeight(int w1,int w2) = 0;
	void setprior(int i){this->prior = i;}
	int getprior(){return this->prior;}
};

template <typename E> // Leaf node subclass
class LeafNode : public HuffNode<E> {
private:
	E it; // Value
	int wgt; // Weight
public:
	LeafNode(const E& val, int freq) // Constructor
	{ it = val; wgt = freq; }
	int weight() { return wgt; }
	E val() { return it; }
	bool isLeaf() { return true; }
	HuffNode<E> *left() const{return nullptr;}
	HuffNode<E> *right() const{return nullptr;}
	void setLeft(HuffNode<E>* node) override {return;}
	void setRight(HuffNode<E>* node) override {return;}
	void setWeight(int w1,int w2) override{return;}
};

template <typename E> // Internal node subclass
class IntlNode : public HuffNode<E> {
private:
	HuffNode<E>* lc; // Left child
	HuffNode<E>* rc; // Right child
	int wgt; // Subtree weight
public:
	IntlNode(HuffNode<E>* l, HuffNode<E>* r)
	{ wgt = l->weight() + r->weight(); lc = l; rc = r; }
	int weight() { return wgt; }
	bool isLeaf() { return false; }
	HuffNode<E>* left() const { return lc; }
	void setLeft(HuffNode<E>* b) override{ lc = (HuffNode<E>*)b; }
	HuffNode<E>* right() const { return rc; }
	void setRight(HuffNode<E>* b) override { rc = (HuffNode<E>*)b; }
	void setWeight(int w1,int w2) override { wgt = w1 + w2; }
};


// HuffTree is a template of two parameters: the element
// type being coded and a comparator for two such elements.
template <typename E>
class HuffTree {	
private:
	HuffNode<E>* Root; // Tree root
public:
	HuffTree(E& val, int freq) // Leaf constructor
	{ Root = new LeafNode<E>(val, freq); }
	// Internal node constructor
	HuffTree(HuffTree<E>* l, HuffTree<E>* r)
	{ Root = new IntlNode<E>(l->root(), r->root()); }
	~HuffTree() {// Destructor
		deleteTree(Root);
	} 
	void deleteTree(HuffNode<E>* node) {
		if (node != nullptr) {
			deleteTree(node->left());
			deleteTree(node->right());
			delete node;
		}
	}
	HuffNode<E>* root() { return Root; } // Get root
	int weight() { return Root->weight(); } // Root weight
	void setRoot(HuffNode<E> *root){ Root = root;} // Set lại gốc mới sau khi cân bằng

	void printTreeHelper(HuffNode<E>* node, int indent) {
        if (node == nullptr) {
            cout << " [Empty Tree]";
            return;
        }

        if (node->isLeaf()) {
            LeafNode<E>* leaf = dynamic_cast<LeafNode<E>*>(node);
            cout << leaf->val() << " (" << leaf->weight() << ")";
        } else {
            IntlNode<E>* internal = dynamic_cast<IntlNode<E>*>(node);
            cout << "Internal Node (" << internal->weight() << ")";
            cout << "\n" << string(indent, ' ') << "Left: ";
            printTreeHelper(internal->left(), indent + 2);
            cout << "\n" << string(indent, ' ') << "Right: ";
            printTreeHelper(internal->right(), indent + 2);
        }
    }
	void printTree(){
		printTreeHelper(Root,0);
		cout << endl;
	}


	//in cây theo inorder
	void printInOrderTree(HuffNode<E> *root){
		if(root){
			printInOrderTree(root->left());
			if(root->isLeaf()){
				LeafNode<E>*leaf = dynamic_cast<LeafNode<E>*>(root);
				cout << leaf->val() << endl;
			}
			else{
				IntlNode<E>* internal = dynamic_cast<IntlNode<E>*>(root);
				cout << internal->weight() << endl;
			}
			printInOrderTree(root->right());
		}
		
	}
	
	// trả về chiều cao
	int getHeight(HuffNode<E> *root){
		if(root == nullptr) return 0;
		return 1 + max(getHeight(root->left()), getHeight(root->right()));
	}
	// trả về cân bằng
	int getBalance(HuffNode<E> *root){
		if(root == nullptr) return 0;
		return getHeight(root->left()) - getHeight(root->right());
	}
	HuffNode<E> *rotateRight(HuffNode<E> *root){
		HuffNode<E> *x = root->left();
		HuffNode<E> *tmp = x->right();
		root->setLeft(tmp);
		x->setRight(root);
		return x;
	}
	HuffNode<E> *rotateLeft(HuffNode<E> *root){
		HuffNode<E> *x = root->right();
		HuffNode<E> *tmp = x->left();
		root->setRight(tmp);
		x->setLeft(root);
		return x;
	}
	//cân bằng cây
	HuffNode<E>* balanceAVL(HuffNode<E>* root) {
		//base case
	    if (root == nullptr) {
	        return root;
	    }
		
		if(getBalance(root) < -1 || getBalance(root) > 1){
			int bal = getBalance(root);
			if (bal > 1) {
				if (getBalance(root->left()) < 0) {
					root->setLeft(rotateLeft(root->left()));
				}
				root = rotateRight(root);
			} 
			else if (bal < -1) {
				if (getBalance(root->right()) > 0) {
					root->setRight(rotateRight(root->right()));
				}
				root = rotateLeft(root);
			}

		}
		root->setLeft(balanceAVL(root->left()));
	    root->setRight(balanceAVL(root->right()));
		
	
	    return root;
	}


	//mã hóa cây
	void buildEncodingTable(HuffNode<E>* node, string code, unordered_map<E, string>& encodingTable) {
        if (node == nullptr) {
            return;
        }

        if (node->isLeaf()) {
            LeafNode<E>* leaf = dynamic_cast<LeafNode<E>*>(node);
            encodingTable[leaf->val()] = code;
        } else {
            IntlNode<E>* internal = dynamic_cast<IntlNode<E>*>(node);
            buildEncodingTable(internal->left(), code + "0", encodingTable);
            buildEncodingTable(internal->right(), code + "1", encodingTable);
        }
    }
	//trả vệ một danh sách chứa kí tự và mã nhị phân
	unordered_map<E, string> buildEncodingTable() {
        unordered_map<E, string> encodingTable;
        buildEncodingTable(Root, "", encodingTable);
        return encodingTable;
    }
    string encode(const string& input,unordered_map<E, string> encodingTable) {
        string encodedString = "";
        for (char c : input) {
            encodedString += encodingTable[c];
        }
        return encodedString;
    }
};



//xây dựng cây huffman
struct minTreeComp {
    template<typename T>
    bool operator()(const T& a, const T& b) const {
        if (a->weight() == b->weight()) {
            // N?u tr?ng s? b?ng nhau, uu tiên theo giá tr? prior
            return a->root()->getprior() > b->root()->getprior();
        }
        return a->weight() > b->weight();
    }
};

template <typename E>
HuffTree<E>* buildHuff(priority_queue<HuffTree<E>*, vector<HuffTree<E>*>, minTreeComp>& forest) {
    HuffTree<E> *temp1, *temp2, *temp3 = nullptr;
    
    while (forest.size() > 1) {
        temp1 = forest.top();
        forest.pop();
        temp2 = forest.top();
        forest.pop();
        temp3 = new HuffTree<E>(temp1, temp2);
        //update prior
        priority_queue<HuffTree<E>*, vector<HuffTree<E>*>, minTreeComp> pq = forest;
		int cnt = 3;
		while(cnt--) {
			temp3->setRoot(temp3->balanceAVL(temp3->root()));
		}
		int res = temp3->weight();
		int p = forest.top()->root()->getprior();
        while(!pq.empty()){
        	HuffTree<E> *tmp = pq.top();
        	pq.pop();
        	if(tmp->weight() > res){
        		break;
			}
        	p++;

		}
        temp3->root()->setprior(p);
        priority_queue<HuffTree<E>*, vector<HuffTree<E>*>, minTreeComp> newForest;
        while (!forest.empty()) {
            HuffTree<E> *tmp = forest.top();
            forest.pop();
            if(tmp->root()->weight() > res) tmp->root()->setprior(++p);
            newForest.push(tmp);
        }
        forest = newForest;
        
        forest.push(temp3);
    }

    return temp3;
}

/*********************************************************************************************************/
//Restaurant 1	
//HashTable phân chia khu vực
template<class T>
class HashTable {
private:
    class Node {
    public:
        T key;
        Node* left;
		Node* right;
        Node(int k) : key(k), left(nullptr),right(nullptr) {}
    };
    Node** hashtable;
	int size;
	queue<int> *qID;//danh sách lưu trữ thứ tự vào của từng khu vực

    
public:
    HashTable(int s) : size(s){
        hashtable = new Node*[size];
		qID = new queue<int>[size];
        for (int i = 0; i < size; ++i) {
            hashtable[i] = nullptr;
        }
    }
    ~HashTable() {
        for (int i = 0; i < size; ++i) {
            delete hashtable[i];
        }
        delete[] hashtable;
    }
	
	//thêm node
    void insertNode(T k,int id) {
		if(id - 1 >= size) return;
        if(hashtable[id - 1] == nullptr){
			hashtable[id - 1] = new Node(k);
		}
		else{
			insertBST(hashtable[id - 1],k);
		}
		qID[id - 1].push(k);
    }
	//nếu xảy ra đụng độ thì thêm vào BST 
    void insertBST(Node *&root,T k){
		if(root == nullptr) root = new Node(k);
		else{
			if(k < root->key) insertBST(root->left,k);
			else if(k >= root->key) insertBST(root->right,k);
		}
	}
	//xóa node
	void deleteBST(Node *&root,T k){
		if(root == nullptr) return;
		else{
			if(k < root->key) deleteBST(root->left,k);
			else if(k > root->key) deleteBST(root->right,k);
			else{
				if(!root->left){
					Node *dlt = root;
					root = root->right;
					delete dlt;
				}
				else if(!root->right){
					Node *dlt = root;
					root = root->left;
					delete dlt;
				}
				else{
					Node *tmp = root->right;
					while(tmp->left) tmp = tmp->left;
					root->key = tmp->key;
					deleteBST(root->right,root->key);
				}
			}
		}
	}
	//dếmd số hoán vị của postorder
	long long int factorial(int n) {
        if (n <= 1)
            return 1;
        return n * factorial(n - 1);
    }

    // Hàm đếm số hoán vị có thể tạo ra cây BST gốc
    long long int countPermutation(vector<int>& postOrder, int start, int end) {
        if (start >= end)
            return 1;

        int root = postOrder[end];
        int i = start;
        while (i < end && postOrder[i] < root)
            i++;

        long long int leftCount = countPermutation(postOrder, start, i - 1);
        long long int rightCount = countPermutation(postOrder, i, end - 1);

        return factorial(end - start) / (factorial(i - start) * factorial(end - i)) * leftCount * rightCount;
    }
	//vector PostOrder
	void getPostOrder(Node *root,vector<int> &v){
		if(root){
			getPostOrder(root->left,v);
			getPostOrder(root->right,v);
			v.push_back(root->key);
		}
	}
	// kokusen
	void deleteID(){
		for(int i = 0;i < size;i++){
			if(!qID[i].empty()){
				vector<int> v;
				getPostOrder(hashtable[i],v);
				// tìm số hoán vị
				long long int per = countPermutation(v, 0, v.size() - 1) % this->size;
				//tiến hành xóa theo FIFO
				for(int j = 0;j < per && !qID[i].empty();j++){
					int key = qID[i].front();
					qID[i].pop();
					deleteBST(hashtable[i],key);
				}
			}
		}
	}
	//hàm in phụ trợ
	void printRecur(Node *root){
		if(root){
			printRecur(root->left);
			cout << root->key << endl;
			printRecur(root->right);
		}
		return;
	}
	//in cây theo inorder
    void printInOrder(int id){
		if(id - 1 >= size || hashtable[id - 1] == nullptr) return;
		printRecur(hashtable[id - 1]);
	}
};


/*nếu node có giá trị bằng nhau thì sắp xếp theo thứ tự vào nhà hàng trước*/
/*********************************************************************************************************/
//nhà hàng 2 dùng min-heap
template <typename E, typename Comp>
class PairHeap : public heap<E, Comp>{
public:
    PairHeap(int maxsize) : heap<E, Comp>(new E[maxsize], 0 , maxsize) {}
	~PairHeap() {delete[] this->Heap;}

	//hàm hỗ trợ
	

	//trả về theo thứ tự sử dụng 
	int getOrder(int label){
		for(unsigned int i = 0;i < this->v.size();i++){
			if(label == this->v[i]) return i;
		}
		return -1;
	}
	//sắp xếp lại theo thứ tự đã sử dụng
	void useOrder(int index){
		int tmp = this->v[index];
		this->v.erase(this->v.begin() + index);
		// đưa vào cuối để xem như mới sử dụng
		this->v.push_back(tmp);
	}
	//trả về số khách tại node 
	int getSize(int label){
		int index = getNodeIndex(label);
		if(index == -1) return 0;
		return this->Heap[index].second.size();
	}



	//insert node dựa vào size của deque
	void insert(const E& it) {
		if(this->size() >= this->maxsize) return;
        int curr = this->plusSize();
        this->Heap[curr] = it; 

		
		//sắp xếp thứ tự sử dụng
		int order = this->Heap[curr].first;
		this->v.push_back(order);
		


        while ((curr != 0) && (Comp::prior(this->Heap[curr].second.size(), this->Heap[this->parent(curr)].second.size()))){
            swap(this->Heap[curr], this->Heap[this->parent(curr)]);
            curr = this->parent(curr);
        }
    }
	void remove(int pos) {
		if (pos == (this->n-1)) this->n--; 
		else
		{
			this->n = this->n - 1;
			swap(this->Heap, pos, this->n); // đổi với phần tứ cuối cùng
			reHeapdown(pos);
		}
	}
	//reheapdown
	void reHeapdown(int index) {
        int pos = index;
        while (!this->isLeaf(pos)) {
            int j = this->leftchild(pos);
            int rc = this->rightchild(pos);
            if ((rc < this->size()) && ((Comp::prior(this->Heap[rc].second.size(), this->Heap[j].second.size()))
			||	(this->Heap[rc].second.size() == this->Heap[j].second.size() 
			&& getOrder(this->Heap[rc].first) < getOrder(this->Heap[j].first))))
                j = rc;
            if (Comp::prior(this->Heap[pos].second.size(), this->Heap[j].second.size()) 
			||(this->Heap[pos].second.size() == this->Heap[j].second.size() && getOrder(this->Heap[pos].first) < getOrder(this->Heap[j].first))) 
				return;
            swap(this->Heap, pos, j);
            pos = j;
        }
    }
	//reheapup
    void reHeapup(int index) {
        int parent = (index - 1) / 2;
        while((index > 0) && ((Comp::prior(this->Heap[index].second.size(),this->Heap[parent].second.size()))
		||	(this->Heap[index].second.size() == this->Heap[parent].second.size() 
		&& 	getOrder(this->Heap[index].first) < getOrder(this->Heap[parent].first)))){
            swap(this->Heap, index, parent);
            index = parent;
            parent = (index - 1) / 2;
        }
    }
	//trả về index ứng với nhãn
	int getNodeIndex(int label) {
        for (int i = 0; i < this->size(); ++i) {
            if (this->Heap[i].first == label) {
                return i;
            }
        }
        return -1; 
    }
	//add khách hàng
	void addValue(int label, int value) {
        int index = getNodeIndex(label);
        if (index != -1) {
            this->Heap[index].second.push_back(value);

			//cập nhật thứ tự
			int order = this->Heap[index].first;
			int num = getOrder(order);
			useOrder(num);
            //reheapdown sau khi đã thêm vào
            this->reHeapdown(index);
        }
    }
	//remove khách theo FIFO
	void removeValue(int label) {
        int index = getNodeIndex(label);
        if (index != -1) {
			int result = this->Heap[index].second.front();
			cout << result << "-" << label << endl;
            this->Heap[index].second.pop_front();
			if(this->Heap[index].second.size() == 0){
				int order = this->Heap[index].first;
				this->v.erase(this->v.begin() + getOrder(order));
				//xóa khỏi heap
				remove(index);
				//nếu không còn khách nữa thì xóa khỏi danh sách sử dụng
				return;
			}
			//cập nhật thứ tự
			int order = this->Heap[index].first;
			int num = getOrder(order);
			useOrder(num);
            //reheapup sau khi đã xóa
            this->reHeapup(index);
			
        }
    }
	//in preorder
	void PreOrderRecur(int index,int num){
		if(index >= this->maxsize) return;
		else{
			int id = this->Heap[index].first;
			deque<int> dq = this->Heap[index].second;
			for(int i = 0;i < num && !dq.empty();i++){
				cout << id << "-" << dq.back() << endl;
				dq.pop_back();
			}
			PreOrderRecur(2 * index + 1,num); //con trái
			PreOrderRecur(2 * index + 2,num); //con phải
		}
	}
	void printPreOrder(int num){
		PreOrderRecur(0,num);
	}
	//so sánh theo số lượng khách rồi tới và chưa sử dụng lâu nhất
	struct Compare {
        PairHeap* pairHeap; 
        Compare(PairHeap* heap) : pairHeap(heap) {}

        bool operator()(const E& a, const E& b) {
            if (a.second.size() == b.second.size()) {
                int n1 = pairHeap->getOrder(a.first);
                int n2 = pairHeap->getOrder(b.first);
                return n1 > n2;
            }
            return a.second.size() > b.second.size();
        }
    };
    void getSmallest(int num) {
        priority_queue<E, vector<E>, Compare> pq(Compare(this));
        for (int i = 0; i < this->size(); ++i) {
            pq.push(this->Heap[i]);
        }
		
        for (int i = 0; i < num && !pq.empty(); ++i) {
            E top = pq.top();
            for(int j = 0;j < num && top.second.size() != 0;j++){
				removeValue(top.first);
			}
            pq.pop();
        }
    }
};




/*********************************************************************************************************/
//solution
class solve{
public:
	// các hàm hỗ trợ
	//mật mã caesar
	string Caesar(const string& name, vector<pair<char,int>> vF) {
		string result = "";
		int n = name.length();
		for (int i = 0; i < n; ++i) {
			char base = isupper(name[i]) ? 'A' : 'a';
			//giá trị cần dịch chuyển
			int shift = isupper(name[i]) ? vF[tolower(name[i]) - 'a' + 26].second : vF[name[i] - 'a'].second;
			result += (name[i] - base + shift) % 26 + base;
		}
		return result;
	}

	//check điều kiện của lapse
	bool checkLapse(string name){
		unordered_set<char> s;
		for(unsigned int i = 0;i < name.length();i++){
			s.insert(name[i]);
		}
		return s.size() >= 3;
	}
	//hàm trả về vector đếm tần suất
	vector<pair<char,int>> getVector(string name){
		int n = name.length();
		vector<pair<char,int>> vF(52,make_pair('0',0));
		for(int i = 0;i < n;i++){
			if(islower(name[i])){
				vF[name[i] - 'a'].first = name[i];
				vF[name[i] - 'a'].second++;
			}
			else{
				vF[tolower(name[i]) - 'a' + 26].first = name[i];
				vF[tolower(name[i]) - 'a' + 26].second++;
			}
		}
		return vF;
	}
	//chuyển từ binary sang decimal
	int BinToDec(int &n){
		int dec = 0;
		int base = 1;
		while(n){
			int digit = n % 10;
			n /= 10;
			dec += digit * base;
			base *= 2;
		}
		return dec;
	}
	//đảo ngược bits
	void reverseStr(string& str)
	{
		int n = str.length();
		for (int i = 0; i < n / 2; i++)
			swap(str[i], str[n - i - 1]);
	}





	/*********************************************************************************************************/
	//Các thuật thức
	void LAPSE(string &name,int maxsize,HashTable<int> *&hashTB,PairHeap<pair<int,deque<int>>,MinHeapComparator> *&mHeap){
		//lấy mảng lưu trữ kí tự và freq của nó
		vector<pair<char,int>> v = getVector(name);

		// tên sau khi mã hóa 
		name = Caesar(name,v);

		//lấy lại mảng mới sau khi đã mã hóa tên
		map<char,int> mp;
		for(auto i : name) mp[i]++;
		vector<pair<char, int>> vF(mp.begin(), mp.end());

		//sắp xếp lại vector theo thứ tự từ viết thường tới viết hoa và theo tần suát
		sort(vF.begin(), vF.end(),[](pair<char, int> a, pair<char, int> b) {
			// so sánh tần suất tăng dần
			if (a.second != b.second) {
				return a.second < b.second;
			}

			// trường hợp bằng freq thì so sánh chữ số 
			if (islower(a.first) && islower(b.first)) {
				return a.first < b.first;
			}

			if (isupper(a.first) && isupper(b.first)) {
				return a.first < b.first;
			}

			// N?u m?t ký t? vi?t hoa, m?t ký t? vi?t thu?ng, ký t? vi?t thu?ng d?n tru?c
			return islower(a.first) ? true : false;
		});
		
		//tạo mảng gồm các lá
		int size = vF.size();
		string code;//mã nhị phân
		int result;//kết quả sau khi lấy nhị phân 
		if(size > 1){
			priority_queue<HuffTree<char>*, vector<HuffTree<char>*>, minTreeComp> charNodesQueue;
			for (int i = 0; i < size; ++i) {
				HuffTree<char> *tmp = new HuffTree<char>(vF[i].first, vF[i].second);
				tmp->root()->setprior(i);
				charNodesQueue.push(tmp);
			}
			
			HuffTree<char>* huffTree = buildHuff(charNodesQueue);

			
			//mã sau khi đi qua cây huffman
			//lấy mã nhị phân của từng kí tự 
			unordered_map<char,string> tmp = huffTree->buildEncodingTable();

			//lấy mã
			code = huffTree->encode(name,tmp);
			
			//đảo ngược lại mã code
			reverseStr(code);
			// cout << code << endl;
			//lấy 10 kí tự đầu của chuỗi sau khi đã đảo ngược(lấy từ phải qua trái theo mã cũ)
			result = stoi(code.substr(0,10));

			//đổi từ nhị phân sang thập phân
			result = BinToDec(result);
		}
		else{
			result = 0;
		}
		//chọn nhà hàng
		int ID = result % maxsize + 1;
		//Nhà S
		if(result % 2  == 0){
			if(mHeap->getSize(ID) == 0){
				pair<int,deque<int>> p = {ID,{result}};
				mHeap->insert(p);
			}
			else{
				mHeap->addValue(ID,result);
			}
		}
		//Nhà G
		else{
			hashTB->insertNode(result,ID);
		}

	}
	void KOKUSEN(HashTable<int> *&hashTB){
		hashTB->deleteID();
	}
	void KEITEIKEN(PairHeap<pair<int,deque<int>>,MinHeapComparator> *&mHeap,int num){
		mHeap->getSmallest(num);
	}
	void HAND(string name){
		vector<pair<char,int>> v = getVector(name);

		// tên sau khi mã hóa 
		name = Caesar(name,v);

		//lấy lại mảng mới sau khi đã mã hóa tên
		map<char,int> mp;
		for(auto i : name) mp[i]++;
		vector<pair<char, int>> vF(mp.begin(), mp.end());

		//sắp xếp lại vector theo thứ tự từ viết thường tới viết hoa và theo tần suát
		sort(vF.begin(), vF.end(),[](pair<char, int> a, pair<char, int> b) {
			// so sánh tần suất tăng dần
			if (a.second != b.second) {
				return a.second < b.second;
			}

			// trường hợp bằng freq thì so sánh chữ số 
			if (islower(a.first) && islower(b.first)) {
				return a.first < b.first;
			}

			if (isupper(a.first) && isupper(b.first)) {
				return a.first < b.first;
			}

			// N?u m?t ký t? vi?t hoa, m?t ký t? vi?t thu?ng, ký t? vi?t thu?ng d?n tru?c
			return islower(a.first) ? true : false;
		});
		
		//tạo mảng gồm các lá
		int size = vF.size();
		if(size > 1){
			priority_queue<HuffTree<char>*, vector<HuffTree<char>*>, minTreeComp> charNodesQueue;
			for (int i = 0; i < size; ++i) {
				HuffTree<char> *tmp = new HuffTree<char>(vF[i].first, vF[i].second);
				tmp->root()->setprior(i);
				charNodesQueue.push(tmp);
			}
			HuffTree<char>* huffTree = buildHuff(charNodesQueue);
			huffTree->printInOrderTree(huffTree->root());
		}
		else{
			cout << vF[0].first << endl;
		}


		
	}
	void LIMITLESS(HashTable<int> *obj,int num){
		obj->printInOrder(num);
	}
	void CLEAVE(PairHeap<pair<int,deque<int>>,MinHeapComparator> *mHeap,int num){
		mHeap->printPreOrder(num);
	}
};

void simulate(string filename)
{
	ifstream input;
	input.open(filename);
	//maxsize
	int maxsize;
	solve obj;
	//khởi tạo các cấu trúc dữ liệu cần xài
	stack<string> st;//lưu danh sách vào nhà hàng của khách
	HashTable<int> *hashTB;//bảng băm lưu trữ khu vực của nhà hàng 1
	PairHeap<pair<int,deque<int>>,MinHeapComparator> *mHeap;//tạo minHeap chưa có khu vực nào
	while(!input.eof()){
		string line;
		getline(input,line);
		stringstream ss(line);
		string str;
		ss >> str;
		if(str == "MAXSIZE"){
			ss >> maxsize;
			hashTB = new HashTable<int>(maxsize);
			mHeap = new PairHeap<pair<int,deque<int>>,MinHeapComparator>(maxsize);
		}
		else if(str == "LAPSE"){
			string name;
			ss >> name;
			if(obj.checkLapse(name) == false) continue;
			st.push(name);
			obj.LAPSE(name,maxsize,hashTB,mHeap);
		}
		else if(str == "KOKUSEN"){
			obj.KOKUSEN(hashTB);
		}
		else if(str == "KEITEIKEN"){
			int num;
			ss >> num;
			obj.KEITEIKEN(mHeap,num);
		}
		else if(str == "HAND"){
			if(!st.empty())
			obj.HAND(st.top());
		}
		else if(str == "LIMITLESS"){
			int num;
			ss >> num;
			obj.LIMITLESS(hashTB,num);
		}
		else if(str == "CLEAVE"){
			int num;
			ss >> num;
			obj.CLEAVE(mHeap,num);
		}

	}
	input.close();
	delete hashTB;
	delete mHeap;
	return;
}