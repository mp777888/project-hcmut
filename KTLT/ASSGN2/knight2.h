#ifndef __KNIGHT2_H__
#define __KNIGHT2_H__

#include "main.h"

// #define DEBUG



class BaseItem;
class BaseKnight;
class BaseBag;

class Events {
public:
    Events( const string & file_events ) ;
    int count() const;
    int get(int i) const;
    ~Events();
private:
    int num_events;  // số lượng sự kiện
    int *event ;  
};



enum ItemType {ANTIDOTE,PHOENIXDOWNI,PHOENIXDOWNII,PHOENIXDOWNIII,PHOENIXDOWNIV};
class BaseItem {
protected:
    ItemType itemType;
public:
    virtual bool canUse ( BaseKnight * knight ) = 0;
    virtual void use ( BaseKnight * knight ) = 0;
    ItemType getitem(){
        return this->itemType;
    }
};
//dslk lưu trữ vật phẩm 
class Node {
public:
    BaseItem* item;
    Node* next;
};
//đổi từ enum về string 
string ItemTypeToString(ItemType itemType);
class BaseBag {
protected:
    BaseKnight* knight;
    Node* head;
    int count;
    int maxItems;
public:
    BaseBag(BaseKnight* knight) : knight(knight), head(NULL), count(0), maxItems(-1) {}
    virtual bool insertFirst(BaseItem * item){
        if(maxItems != -1 && count >= maxItems) {
            return false;
        }
        Node* newNode = new Node;
        newNode->item = item;
        newNode->next = head;
        head = newNode;
        count++;
        return true;
    }
    virtual BaseItem * get(ItemType itemType) {
        if(head == NULL)
        return NULL;
        Node* current = head;
        Node* previous = NULL;
        while(current != NULL) {
            if(current->item->getitem() == itemType) {
                // thay đổi vật phẩm cần xài vào đầu danh sách
                if(previous != NULL) {
                    previous->next = current->next;
                    current->next = head;
                    head = current;
                }
                current = head;
                head = head->next;
                BaseItem* item = current->item;
                delete current;
                count--;
                return item;
            }
            previous = current;
            current = current->next;
        }
        return NULL; 
    }
    //in ra ds vật phẩm 
    virtual string toString() {
        string result = "Bag[count=" + to_string(count) + ";";
        Node* current = head;
        while (current != nullptr) {
            result += ItemTypeToString(current->item->getitem());
            if (current->next != nullptr) {
                result += ",";
            }
            current = current->next;
        }
        result += "]";
        return result;
    }
    // xóa 3 món đồ gần nhất
    void remove() {
        for (int i = 0; i < 3; ++i) {
            if (head == nullptr) { 
                break;
            }
            Node* temp = head;
            head = head->next;
            count--;
            delete temp->item;
            delete temp;
        }
    }
    BaseItem *getFirstItem(BaseKnight *knight){
    Node* current = head;
    while(current != NULL) {
        if(current->item->canUse(knight)) {
            return current->item;
        }
        current = current->next;
    }
        return NULL;
    }
};

class BaseOpponent{
    public:
        virtual void fight(BaseKnight *knight) = 0;
};

enum KnightType { PALADIN = 0, LANCELOT, DRAGON, NORMAL };
class BaseKnight {
protected:
    int id;
    int hp;
    int maxhp; //const
    int level;
    int gil;
    int antidote;
    BaseBag * bag;
    KnightType knightType;
    int i ;
    int eventid;
private:
    bool po = false;//có bị nhiễm độc hay không

public:
    static BaseKnight * create(int id, int maxhp, int level, int gil, int antidote, int phoenixdownI);
    string toString() const;
    //getter trả về loại hiệp sĩ
    KnightType getKnightType() const {
        return knightType;
    }
    //thành phần của từng đối tượng trong mảng động
    void setid(int id){
        this->id = id;
    }
    void setHP(int hp){
        this->hp = hp;
    }
    void setmaxhp(int maxhp){
        this->maxhp = maxhp;
    }
    void setlevel(int level){
        this->level = level;
    }
    void setgil(int gil){
        this->gil = gil;
    }
    void setantidote(int antidote){
        this->antidote = antidote;
    }
    //không có thuốc antidote
    void setPo(bool po){
        this->po = po;
    }
    void seti(int i){
        this->i = i;
    }
    void seteventid(int eventid){
        this->eventid = eventid;
    }

    // liên quan tới túi đồ
    void setBag(BaseBag *bag) {
        this->bag = bag;
    }
    void deleteItem(BaseKnight *knight){
        knight->bag->remove();
    }
    bool insert(BaseItem *item,BaseKnight *knight){
        return knight->bag->insertFirst(item);
    }
    BaseItem *getItem(BaseKnight *knight,ItemType itemType){
        return knight->bag->get(itemType);
    }
    BaseItem *getFirst(BaseKnight *knight){
        return knight->bag->getFirstItem(knight);
    }
    /////////////////////////
    //trả về sự kiện
    int geteventid(){
        return this->eventid;
    }
    //trả về thứ tự sự kiện
    int geti(){
        return this->i;
    }
    //trả về hiệu ứng độc
    bool Posioned(){
        return this->po;
    }

    // trả về thông tin
    int gethp(){
        return this->hp;
    }
    int getmaxhp(){
        return this->maxhp;
    }
    int getlevel(){
        return this->level;
    }
    int getgil(){
        return this->gil;
    }
};

class ArmyKnights {
public:
    ArmyKnights (const string & file_armyknights);
    ~ArmyKnights();
    bool fight(BaseOpponent * opponent);
    bool adventure (Events * events); // đánh bại boss
    int count() const;
    void giamHS();// giảm số lượng hiệp sĩ khi có hs hi sinh
    BaseKnight * lastKnight() const;// hiệp sĩ cuối
    BaseKnight * KnightCount(int i);// hiệp sĩ thứ i
    bool hasPaladinShield() const;
    bool hasLancelotSpear() const;
    bool hasGuinevereHair() const;
    bool hasExcaliburSword() const;

    void printInfo() const;
    void printResult(bool win) const;

    void set95(bool check95) {
        this->check95 = check95;
    }
    void set96(bool check96){
        this->check96 = check96;
    }
    void set97(bool check97){
        this->check97 = check97;
    }
    void set98(bool check98){
        this->check98 = check98;
    }
    bool get95() const{
        return this->check95;
    }
    bool get96() const{
        return this->check96;
    }
    bool get97() const{
        return this->check97;
    }
    bool get98() const{
        return this->check98;
    }

private:
    int num_knights; // số lượng hiệp sĩ còn sống
    int demHS;
    BaseKnight **knights;
    bool check95 = false;
    bool check96 = false;
    bool check97 = false;
    bool check98 = false;
};







class KnightAdventure {
private:
    ArmyKnights * armyKnights;
    Events * events;

public:
    KnightAdventure();
    ~KnightAdventure();

    void loadArmyKnights(const string &);
    void loadEvents(const string &);
    void run();
};

#endif // __KNIGHT2_H__