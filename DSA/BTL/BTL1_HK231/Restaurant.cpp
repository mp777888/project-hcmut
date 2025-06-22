#include "main.h"





template<class T>
class Stack{
private:
	T *head;
	int count;
public:
	Stack() :head(nullptr),count(0){}
	~Stack(){
		while(!isEmpty())
			pop();
	}
	bool isEmpty(){
		return count == 0;
	}
	void push(T *cus){
		Restaurant::customer *newcus = new Restaurant::customer(cus->name,cus->energy,nullptr,nullptr);
        if(isEmpty()) {
            head = newcus;
        }
		else if(!findCus(newcus)){
            T* tmp = head;
            while (tmp->next) {
                tmp = tmp->next;
            }
            tmp->next = newcus;
            newcus->prev = tmp;
        }
		else return;
		count++;
	}
	void pop(){
    if (!isEmpty()) {
        Restaurant::customer *tmp = top();
        if (tmp->prev) {
            tmp->prev->next = nullptr;
        }
		else {
            head = nullptr;
        }
        count--;
    }
}

	Restaurant::customer *top(){
		Restaurant::customer *tmp = head;
		while(tmp->next){
			tmp = tmp->next;
		}
		return tmp;
	}
	bool findCus(T *newcus){
		Restaurant::customer *tmp = head;
		while(tmp){
			if(tmp->name == newcus->name) return true;
			tmp = tmp->next;
		}
		return false;
	}
	void printQ() {
		if(count == 0) return;
        T* cur = head;
        while (cur) {
            cur->print();
            cur = cur->next;
        }
    }
};






//hàng đợi khách hàng
template <class T>
class Queue {
private:
    T* head;
    int count;

public:
    Queue() : head(nullptr), count(0) {}

    ~Queue() {
        clear();
    }

    bool isEmpty() const {
        return count == 0;
    }

    void enqueue(T* cus) {
		Restaurant::customer *newcus = new Restaurant::customer(cus->name,cus->energy,nullptr,nullptr);
        if(isEmpty()) {
            head = newcus;
        }
		else if(!findCus(newcus)){
            T* tmp = head;
            while (tmp->next) {
                tmp = tmp->next;
            }
            tmp->next = newcus;
            newcus->prev = tmp;
        }
		else return;
		count++;
    }
    void dequeue() {
        if (!isEmpty()) {
            T* tmp = head;
            head = head->next;
            if (head) {
                head->prev = nullptr;
            }
            count--;
        }
    }
	void clear(){
		while(!isEmpty()) dequeue();
	}
	void delCus(int n){
		if(n == 0) dequeue();
		else{
			Restaurant::customer *tmp = head;
			for(int i = 0;i < n;i++){
				tmp = tmp->next;
			}
			tmp->prev->next = tmp->next;
			if(tmp->next) tmp->next->prev = tmp->prev;
			count--;
		}
	}
	bool findCus(T *newcus){
		Restaurant::customer *tmp = head;
		while(tmp){
			if(tmp->name == newcus->name) return true;
			tmp = tmp->next;
		}
		return false;
	}
	int findPos(T *newcus){
		Restaurant::customer *tmp = head;
		int i = 0;
		while(tmp){
			if(tmp->name == newcus->name) return i;
			i++;
			tmp = tmp->next;
		}
		return -1;
	}
    Restaurant::customer* front(){
        return head;
    }
	T *findMin(){
		Restaurant::customer *cur = head;
		Restaurant::customer *tmp;
		int minE = 2147483647;
		while(cur){
			if(cur->energy < minE){
				minE = cur->energy;
				tmp = cur;
			}
			cur = cur->next;
		}
		return tmp;
	}
    void printQ() {
		if(count == 0) return;
        T* cur = head;
        while (cur) {
            cur->print();
            cur = cur->next;
        }
    }
	int size(){
		return count;
	}
	void copyQ(Queue<T> &q) {
    T* current = head;
    while (current) {
        T *newcus = new T(current->name, current->energy, nullptr, nullptr);
        q.enqueue(newcus);
        current = current->next;
    }
}

};


class CLinkedList{
private:
    Restaurant::customer* tail;
	Queue<Restaurant::customer> *q;// hàng đợi khách
	Queue<Restaurant::customer> *qTime; // thời gian vào của hàng đợi(domain)
	Queue<Restaurant::customer> *curCus; //xếp theo thứ tự vào hàng trước
    int count;//số lượng khách
	int x;//vị trí có sự thay đổi
public:
    CLinkedList() : tail(nullptr), count(0) {
		q = new Queue<Restaurant::customer>();
		qTime = new Queue<Restaurant::customer>();
		curCus = new Queue<Restaurant::customer>();
	}
    ~CLinkedList() {
		if(count != 0) clearCus();

	}

	//hàm phụ trợ
	bool findCustomer(string name){
			if(count == 0) return false;
			Restaurant::customer *tmp = tail->next;
			do{
				if(tmp->name == name) return true;
				tmp = tmp->next;
			}
			while(tmp != tail->next);
			return false;
		}
	int findX(Restaurant::customer *cus){
			Restaurant::customer *tmp = tail->next;
			for(int i = 0;i < count;i++){
				if(tmp->name == cus->name) return i;
				tmp = tmp->next;
			}
			return 0;
		}


	// RED
	void addCustomer(Restaurant::customer* newcus){
		if(MAXSIZE == 0 || newcus->energy == 0) return;
		if(count == 0 ){
			tail = newcus;
            tail->prev = newcus;
            tail->next = newcus;
			x = 0;
			count = 1;
			curCus->enqueue(newcus);
		}
		//khong bi trung ten
		if(!findCustomer(newcus->name)){

			if(count < MAXSIZE){

				if(count >= MAXSIZE / 2){
					int res = 0;
					Restaurant::customer *tmp = tail->next;
					for(int i  = 0;i < x;i++) tmp = tmp->next;
					Restaurant::customer *firstX = tmp,*lastX = tmp;
					Restaurant::customer *pC;
					do{
						if(abs(newcus->energy - firstX->energy) > abs(res)){
							res = newcus->energy - firstX->energy;
							pC = firstX;
						}
						firstX = firstX->next;
					}
					while(firstX != lastX);
					Restaurant::customer *cur = tail->next;
					x = 0;
					for(int i = 0;cur != pC;i++) {
						x = i + 1;
						cur = cur->next;
					}

					if(res >= 0){
						if(count == 1){
							newcus->next = tail;
							newcus->prev = tail;
							tail->prev = newcus;
							tail->next = newcus;

						}
						else{
							newcus->prev = cur;
							newcus->next = cur->next;
							cur->next->prev = newcus;
							cur->next = newcus;
							if(x == count - 1) tail->next = newcus;
						}
						x++;
					}
					else if(res < 0){
						if(count == 1){

							newcus->next = tail;
							newcus->prev = tail;
							tail->prev = newcus;
							tail->next = newcus;
							tail = newcus;
						}
						else{
							Restaurant::customer *previous = cur->prev;
							newcus->prev = previous;
							newcus->next = previous->next;
							previous->next->prev = newcus;
							previous->next = newcus;
							if(x == 0) tail = newcus;
						}
					}


				}
				else if(count < MAXSIZE){
					Restaurant::customer *cur = tail->next;
					for(int i = 0;i < x;i++){
						cur = cur->next;
					}
					if(cur->energy <= newcus->energy){
						if(count == 1){
							newcus->next = tail;
							newcus->prev = tail;
							tail->prev = newcus;
							tail->next = newcus;

						}
						else{
							newcus->prev = cur;
							newcus->next = cur->next;
							cur->next->prev = newcus;
							cur->next = newcus;
							if(x == count - 1) tail->next = newcus;
						}
					}
					else if(cur->energy > newcus->energy){
						if(count == 1){
							newcus->next = tail;
							newcus->prev = tail;
							tail->prev = newcus;
							tail->next = newcus;
							tail = newcus;
						}
						else{
							Restaurant::customer *previous = cur->prev;
							newcus->prev = previous;
							newcus->next = previous->next;
							previous->next->prev = newcus;
							previous->next = newcus;
						}
					}
				}
				// cập nhật x
				Restaurant::customer *newhead = tail->next;
				x = 0;
				for(int i = 0;newhead != newcus;i++){
					newhead = newhead->next;
					x = i + 1;
				}
				curCus->enqueue(newcus);
				count++;
			}
			else if(count >= MAXSIZE && q->size() < MAXSIZE){
				q->enqueue(newcus);
				qTime->enqueue(newcus);
				curCus->enqueue(newcus);
			}

		}
		else return;
	}




	//BLUE
	void removeCustomer(int num){
		//xóa khách trong queue curcus
		if(count == 0) return;
		else if(num >= count || num > MAXSIZE){
			clearCus();
		}
		else{
			for(int i = 0;i < num;i++){
				Restaurant::customer *del = curCus->front();
				while(!findCustomer(del->name)){
					del = del->next;
				}
				x = findX(del);
				curCus->delCus(curCus->findPos(del));
				if(x == 0){
					Restaurant::customer *tmp = tail->next;
					if(tmp == tail){
						free(tail);
						tail = nullptr;
					}
					tail->next = tmp->next;
					tmp->next->prev = tail;
					free(tmp);
					tmp = nullptr;
				}
				else if(x == count - 1){
					Restaurant::customer *tmp = tail->prev;
					if(tmp == tail){
						free(tail);
						tail = nullptr;
					}
					tmp->next = tail->next;
					tail->next->prev = tmp;
					free(tail);
					tail = tmp;
				}
				else{
					Restaurant::customer *tmp = tail->next;
					for(int i = 0;i < x;i++) tmp = tmp->next;
					tmp->prev->next = tmp->next;
					tmp->next->prev = tmp->prev;
					free(tmp);
					tmp = nullptr;
					if(tmp == tail) tail = tmp->prev;
				}



				//cập nhật lại x
				if(x == count - 2){
					if(count == 1) x = 0;
					else if(del->energy > 0){
						if(x == count - 1) x = 0;
					}
					else if(del->energy < 0){
						if(x == 0) x = count - 1;
						else x = x - 1;
					}
					count--;
				}
				else{
					count--;
					if(count == 1) x = 0;
					else if(del->energy > 0){
						if(x == count - 1) x = 0;
					}
					else if(del->energy < 0){
						if(x == 0) x = count - 1;
						else x = x - 1;
					}

				}
			}
		}
		//thêm khách từ hàng đợi
		while(!q->isEmpty() && count < MAXSIZE){
			Restaurant::customer *tmp = new Restaurant::customer(q->front()->name,q->front()->energy,nullptr,nullptr);
			addCustomer(tmp);
			//xóa khỏi hàng đợi
			q->dequeue();
			qTime->delCus(qTime->findPos(tmp));
		}
	}
	void clearCus(){
		if (count == 0) {
			return;
		}
		Restaurant::customer *cur = tail->next;
		do {
			Restaurant::customer *tmp = cur;
			curCus->delCus(curCus->findPos(tmp));
			cur = cur->next;
			delete tmp;
		}
		while (cur != tail->next);
		tail = nullptr;
		count = x = 0;
	}





	//PURPLE
	void moveptr(Restaurant::customer  *&ptr,int dis){
		ptr = q->front();
		for(int i = 0;i < dis;i++) ptr = ptr->next;
	}
	void swap(Restaurant::customer *&ptr,int i,int k,int &N){
		moveptr(ptr,k);
		string name1 = ptr->name;
		int energy1 = ptr->energy;
		moveptr(ptr,i);
		string name2 = ptr->name;
		int energy2 = ptr->energy;
		ptr->name = name1;
		ptr->energy = energy1;
		moveptr(ptr,k);
		ptr->name = name2;
		ptr->energy = energy2;
		N++;
	}
	bool comp(Restaurant::customer *ptr,int i,int j){
		moveptr(ptr,i);
		int a = ptr->energy;
		int pos1 = qTime->findPos(ptr);
		moveptr(ptr,j);
		int b = ptr->energy;
		int pos2 = qTime->findPos(ptr);
		if(abs(a) == abs(b)){
			if(pos1 > pos2) return false;
			else return true;
		}
		return abs(a) > abs(b);
	}
	void inssort2(Restaurant::customer *ptr,int n,int incr,int &N){
		for (int i = incr; i < n; i++)
			for (int j = i; j >= incr && comp(ptr,j,j - incr);j -= incr)
				swap(ptr,j,j - incr,N);
	}
	void shellsort(){
		if(q->size() == 0) return;
		int maxE = 0,size;
		Restaurant::customer *cur = q->front();
		Restaurant::customer *prev = nullptr;
		for(int i = 1;cur;i++){
			if(maxE <= abs(cur->energy)){
				if(maxE == abs(cur->energy) && qTime->findPos(cur) < qTime->findPos(prev)){
					cur = cur->next;
					continue;
				}
				prev = cur;
				size = i;
				maxE = abs(cur->energy);
			}
			cur = cur->next;
		}
		int N = 0;

		Restaurant::customer *tmp = q->front();
		for(int i = size / 2;i > 2;i /= 2){
			for(int j = 0;j < i;j++)
				inssort2(tmp,size - j,i,N);
		}
		inssort2(tmp,size,1,N);
		removeCustomer(N % MAXSIZE);
	}



	//REVERSAL
	void reversal(){
		if(count == 0) return;
		Restaurant::customer *tmp = tail->next;
		for(int i = 0;i < x;i++) tmp = tmp->next;
		Restaurant::customer *lastX = tmp;
		// Restaurant::customer *pC = new Restaurant::customer(tmp->name,tmp->energy,nullptr,nullptr);//vị trí hiện tại của x
		string tmpname = tmp->name;
		Stack<Restaurant::customer> *stP = new Stack<Restaurant::customer>;//khách dương
		Stack<Restaurant::customer> *stN = new Stack<Restaurant::customer>;//khách âm
		do{
			if(lastX->energy > 0) stP->push(lastX);
			else if(lastX->energy < 0) stN->push(lastX);
			lastX = lastX->prev;

		}
		while(lastX != tmp);
		reversalCus(stP,stN);

		//cập nhật lại x
		Restaurant::customer *cur = tail->next;
		x = 0;
		for(int i = 0;i < count;i++){
			x = i;
			if(cur->name == tmpname) break;

			cur = cur->next;
		}
	}
	void reversalCus(Stack<Restaurant::customer> *stP,Stack<Restaurant::customer> *stN){
		Restaurant::customer *tmp = tail->next;
		for(int i = 0;i < x;i++) tmp = tmp->next;
		Restaurant::customer *lastX = tmp;
		do{
			if(lastX->energy > 0 && !stP->isEmpty()){
				Restaurant::customer *cusR = stP->top();
				lastX->name = cusR->name;
				lastX->energy = cusR->energy;
				stP->pop();
			}
			else if(lastX->energy < 0 && !stN->isEmpty()){
				Restaurant::customer *cusR = stN->top();
				lastX->name = cusR->name;
				lastX->energy = cusR->energy;
				stN->pop();
			}
			lastX = lastX->prev;
		}
		while(lastX != tmp);
	}



	//Unlimited
	void longChain(){
		if(count < 4) return;
		Queue<Restaurant::customer> *qL = new Queue<Restaurant::customer>();
		Restaurant::customer *tmp = tail->next;
		for(int i = 0;i < x;i++) tmp = tmp->next;
		Restaurant::customer *lastX = tmp;// vị trí x
		int minRes = 2147483647;//INT_MAX
		do{
			Restaurant::customer *firstX = tmp;
			int res = 0;
			Queue<Restaurant::customer> *qT = new Queue<Restaurant::customer>();
			for(int i = 0;i < count;i++){
				res += firstX->energy;
				qT->enqueue(firstX);
				if(qT->size() >= 4){
					if(res < minRes || (res == minRes && qT->size() >= qL->size())){
						minRes = res;
						qL->clear();
						qT->copyQ(*qL);
					}
				}
				firstX = firstX->next;
			}
			tmp = tmp->next;
		}
		while(tmp != lastX);


		//in danh sách
		int cntQ = 0;
		Restaurant::customer *current = tail->next;
		while(current->name != qL->findMin()->name) current = current->next;
		while(cntQ < qL->size()){
			if(qL->findPos(current) != -1){
				current->print();
				cntQ++;
			}
			current = current->next;
		}
	}




	//Domain
	void kick(){
		if(count == 0) return;

		long long int sumP = 0;//energy dương
		long long int sumN = 0;//energy dương và âm
		Restaurant::customer *tmp = tail->next;
		do{
			if(tmp->energy > 0) sumP += tmp->energy;
			else if(tmp->energy < 0) sumN += tmp->energy;
			tmp = tmp->next;
		}
		while(tmp != tail->next);

		Restaurant::customer *temp = q->front();
		while(temp){
			if(temp->energy > 0) sumP += temp->energy;
			else if(temp->energy < 0) sumN += temp->energy;
			temp = temp->next;
		}

		//kick khách
		if(sumP < abs(sumN)){
			Stack<Restaurant::customer> *stP = new Stack<Restaurant::customer>();
			Restaurant::customer *clP = curCus->front();
			//vào trước thì ra trước

			while(clP ){
				if(clP->energy > 0){
                    stP->push(clP);
                    if(findCustomer(clP->name)){
                        //xóa khỏi danh sách
                        x = findX(clP);

                        if(x == 0){
                            Restaurant::customer *del = tail->next;
                            if(del == tail || count == 1){
                                free(tail);
                                tail = nullptr;
                            }
                            else{
                                tail->next = del->next;
                                del->next->prev = tail;
                                free(del);
                                del = nullptr;
                            }
                        }

                        else if(x == count - 1){
                            Restaurant::customer *del = tail->prev;
                            if(del == tail || count == 1){
                                free(del);
                                del = nullptr;
                            }
                            else{
                                del->next = tail->next;
                                tail->next->prev = del;
                                free(tail);
                                tail = del;
                            }
                        }
                        else{
                            Restaurant::customer *del = tail->next;
                            for(int i = 0;i < x;i++) del = del->next;
                            del->prev->next = del->next;
                            del->next->prev = del->prev;
                            free(del);
                            del = nullptr;
                            if(del == tail) tail = del->prev;
                        }
                        //cập nhật lại vị trí x
                        if(x == count - 2){
                            if(x == count - 1) x = 0;
                            count--;
                        }
                        else{
                            count--;
                            if(x == count - 1) x = 0;
                        }

                    }
					//xóa khỏi hàng đợi
					else if(q->findCus(clP)){
                        int pos = q->findPos(clP);
                        int pos2 = qTime->findPos(clP);
                        q->delCus(pos);
                        qTime->delCus(pos2);
					}
					int pos3 = curCus->findPos(clP);
					curCus->delCus(pos3);
				}
				clP = clP->next;
			}






			//in ra danh sách
			while(!stP->isEmpty()){

				stP->top()->print();
				stP->pop();

			}
		}


		else if(sumP >= abs(sumN)){
			Stack<Restaurant::customer> *stN = new Stack<Restaurant::customer>();
			Restaurant::customer *clN = curCus->front();

			//nhập vào để in ra
			while(clN){
				if(clN->energy < 0){
                    stN->push(clN);
                    if(findCustomer(clN->name)){

                        //xóa khỏi danh sách
                        x = findX(clN);
                        if(x == 0){
                            Restaurant::customer *del = tail->next;
                            if(del == tail){
                                free(tail);
                                tail = nullptr;
                            }
                            tail->next = del->next;
                            del->next->prev = tail;
                            free(del);
                            del = nullptr;
                        }
                        else if(x == count - 1){
                            Restaurant::customer *del = tail->prev;
                            if(del == tail){
                                free(del);
                                del = nullptr;
                            }
                            del->next = tail->next;
                            tail->next->prev = del;
                            free(tail);
                            tail = del;
                        }
                        else{
                            Restaurant::customer *del = tail->next;
                            for(int i = 0;i < x;i++) del = del->next;
                            del->prev->next = del->next;
                            del->next->prev = del->prev;
                            free(del);
                            del = nullptr;
                            if(del == tail) tail = del->prev;
                        }
                        //cập nhật lại vị trí x
                        if(x == count - 2){
                            if(x == 0) x = count - 1;
                            else x = x - 1;
                            count--;
                        }
                        else{
                            count--;
                            if(x == 0) x = count - 1;
                            else x = x - 1;
                        }
                    }
                    else if(q->findCus(clN)){
                        int pos = q->findPos(clN);
                        int pos2 = qTime->findPos(clN);
                        q->delCus(pos);
                        qTime->delCus(pos2);
                    }
					//xóa khỏi hàng đợi
					int pos3 = curCus->findPos(clN);
					curCus->delCus(pos3);
				}
				clN = clN->next;
			}





			//in ra danh sách
			while(!stN->isEmpty()){
				stN->top()->print();
				stN->pop();
			}
		}

		//thêm khách từ hàng đợi
		while(!q->isEmpty() && count < MAXSIZE){
			Restaurant::customer *tmp = new Restaurant::customer(q->front()->name,q->front()->energy,nullptr,nullptr);
			addCustomer(tmp);
			//xóa khỏi hàng đợi
			q->dequeue();
			qTime->delCus(qTime->findPos(tmp));

		}
	}


	//light num
	void printLight(int num){
		if(tail == nullptr) return;
		if(num > 0){
			Restaurant::customer *cur = tail->next;
			for(int i = 0;i < x;i++) cur = cur->next;
			Restaurant::customer *lastX = cur;
			do{
				cur->print();
				cur = cur->next;
			}
			while(cur != lastX);
		}
		else if(num < 0){
			Restaurant::customer *cur = tail->next;
			for(int i = 0;i < x;i++) cur = cur->next;
			Restaurant::customer *lastX = cur;
			do{
				cur->print();
				cur = cur->prev;
			}
			while(cur != lastX);
		}
		else if(num == 0){
			q->printQ();
		}
	}
};






class imp_res : public Restaurant
{
	private:
		CLinkedList *cl ;
	public:
		imp_res() {
			cl = new CLinkedList();
		};
		~imp_res(){
			delete cl;
		}
		void RED(string name, int energy)
		{
			customer *cus = new customer (name, energy, nullptr, nullptr);
			cl->addCustomer(cus);
		}
		void BLUE(int num)
		{
			cl->removeCustomer(num);
		}
		void PURPLE()
		{
			cl->shellsort();
		}
		void REVERSAL()
		{
			cl->reversal();
		}
		void UNLIMITED_VOID()
		{
			cl->longChain();
		}
		void DOMAIN_EXPANSION()
		{
			cl->kick();
		}
		void LIGHT(int num)
		{
			cl->printLight(num);
		}
};
