#include "knight2.h"
/* * * class Events * * */
string ItemTypeToString(ItemType itemType) {
    switch (itemType) {
        case ANTIDOTE: return "Antidote";
        case PHOENIXDOWNI: return "PhoenixI";
        case PHOENIXDOWNII: return "PhoenixII";
        case PHOENIXDOWNIII: return "PhoenixIII";
        case PHOENIXDOWNIV: return "PhoenixIV";
    }
    return "";
}
Events::Events(const string & file_events){
    ifstream file; 
    file.open(file_events);
    file >> num_events; // số lượng sự kiện
    event = new int[num_events];
    for(int i = 0;i < num_events;i++){ 
        file >> event[i]; //truyền dữ liệu vào con trỏ lưu trữ sự kiện
    }
    file.close();
}
// số lượng sự kiện
int Events::count() const{
    return this->num_events; 
}

// sự kiện thứ i mà hiệp sĩ phải gặp
int Events::get(int i) const{
    return event[i];
}
Events::~Events(){
    delete[] event;
}
/* END class Events */


/* * * BEGIN implementation of class BaseItem * * */
class Antidote : public BaseItem{
    public:
        Antidote(){
            itemType = ANTIDOTE;
        }
        bool canUse ( BaseKnight * knight ){
            if(knight->Posioned() == true) return true;
            return false;
        }
        void use ( BaseKnight * knight ){
            knight->setPo(false);
        }
};
class PhoenixDownI : public BaseItem{
    public:
        PhoenixDownI(){
            itemType = PHOENIXDOWNI;
        }
        bool canUse ( BaseKnight * knight ){
            return knight->gethp() <= 0;
        }
        void use ( BaseKnight * knight ){
            knight->setHP(knight->getmaxhp());
        }

};
class PhoenixDownII : public BaseItem{
    public:
        PhoenixDownII(){
            itemType = PHOENIXDOWNII;
        }
        bool canUse ( BaseKnight * knight ){
            return knight->gethp() <= knight->getmaxhp() / 4;
        }
        void use ( BaseKnight * knight ){
            knight->setHP(knight->getmaxhp());
        }
};
class PhoenixDownIII : public BaseItem{
    public:
        PhoenixDownIII(){
            itemType = PHOENIXDOWNIII;
        }
        bool canUse ( BaseKnight * knight ){
            return knight->gethp() < knight->getmaxhp() / 3;
        }
        void use ( BaseKnight * knight ){
            if(knight->gethp() <= 0) knight->setHP(knight->getmaxhp() / 3);
            else knight->setHP(knight->gethp() + knight->getmaxhp() / 4);
        }
};
class PhoenixDownIV : public BaseItem{
    public:
        PhoenixDownIV(){
            this->itemType = PHOENIXDOWNIV;
        }
        bool canUse ( BaseKnight * knight ){
            return knight->gethp() < knight->getmaxhp() / 2;
        }
        void use ( BaseKnight * knight ){
            if(knight->gethp() <= 0) knight->setHP(knight->getmaxhp() / 2);
            else knight->setHP(knight->gethp() + knight->getmaxhp() / 5);
        }
};
/* * * END implementation of class BaseItem * * */


/* * * BEGIN implementation of class BaseBag * * */

class DragonBag : public BaseBag{
    public:
        DragonBag(BaseKnight *knight,int phoenixdownI,int antidote): BaseBag(knight){
            maxItems = 14;
            for(int i = 0; i < phoenixdownI; i++) {
                Node* newNode = new Node;
                newNode->item = new PhoenixDownI();
                newNode->next = head;
                head = newNode;
                count++;
            }
        }
};
class LancelotBag : public BaseBag{
    public:
        LancelotBag(BaseKnight *knight,int phoenixdownI,int antidote) : BaseBag(knight) {
            maxItems = 16;
            for(int i = 0; i < phoenixdownI; i++) {
                Node* newNode = new Node;
                newNode->item = new PhoenixDownI();
                newNode->next = head;
                head = newNode;
                count++;
            }
            for(int i = 0; i < antidote; i++) {
                Node* newNode = new Node;
                newNode->item = new Antidote();
                newNode->next = head;
                head = newNode;
                count++;
            }
        }
};
class PaladinBag : public BaseBag{
    public:
        PaladinBag(BaseKnight *knight,int phoenixdownI,int antidote) : BaseBag(knight){
            maxItems = -1;
            for(int i = 0; i < phoenixdownI; i++) {
                Node* newNode = new Node;
                newNode->item = new PhoenixDownI();
                newNode->next = head;
                head = newNode;
                count++;
            }
            for(int i = 0; i < antidote; i++) {
                Node* newNode = new Node;
                newNode->item = new Antidote();
                newNode->next = head;
                head = newNode;
                count++;
            }
        }
};
class NormalBag : public BaseBag{
    public:
        NormalBag(BaseKnight *knight,int phoenixdownI,int antidote) : BaseBag(knight){
            maxItems = 19;
            for(int i = 0; i < phoenixdownI; i++) {
                Node* newNode = new Node;
                newNode->item = new PhoenixDownI();
                newNode->next = head;
                head = newNode;
                count++;
            }
            for(int i = 0; i < antidote; i++) {
                Node* newNode = new Node;
                newNode->item = new Antidote();
                newNode->next = head;
                head = newNode;
                count++;
            }
        }
};



/* * * END implementation of class BaseBag * * */
/* * * */

/* * * BEGIN implementation of class BaseOpponent * * */
//1
class MadBear : public BaseOpponent{
    private:
        int basegil = 100;
        int basedamage = 10;
    public:
        void fight(BaseKnight *knight) override{
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            if(level >= levelO){
                knight->setgil(knight->getgil() + basegil);
            }
            else if(level < levelO){
                HP = HP - basedamage*(levelO - level);
                knight->setHP(HP);
            }
        }
};
//2
class Bandit : public BaseOpponent{
   private:
        int basegil = 150;
        int basedamage = 15;
    public:
        void fight(BaseKnight *knight) override{
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            if(level >= levelO){
                knight->setgil(knight->getgil() + basegil);
            }
            else if(level < levelO){
                HP = HP - basedamage*(levelO - level);
                knight->setHP(HP);
            }
        }
};
//3
class LordLupin : public BaseOpponent{
    private:
        int basegil = 450;
        int basedamage = 45;
    public:
        void fight(BaseKnight *knight) override{
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            if(level >= levelO){
                knight->setgil(knight->getgil() + basegil);
            }
            else if(level < levelO){
                HP = HP - basedamage*(levelO - level);
                knight->setHP(HP);
            }
        }
};
//4
class Elf : public BaseOpponent{
  private:
        int basegil = 750;
        int basedamage = 75;
    public:
        void fight(BaseKnight *knight) override{
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            if(level >= levelO){
                knight->setgil(knight->getgil() + basegil);
            }
            else if(level < levelO){
                HP = HP - basedamage*(levelO - level);
                knight->setHP(HP);
            }
        }
};
//5
class Troll : public BaseOpponent{
   private:
        int basegil = 800;
        int basedamage = 95;
    public:
        void fight(BaseKnight *knight) override{
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            if(level >= levelO){
                knight->setgil(knight->getgil() + basegil);
            }
            else if(level < levelO){
                HP = HP - basedamage*(levelO - level);
                knight->setHP(HP);
            }
        }
};
//6
class Tornbery : public BaseOpponent{
    public:
        void fight(BaseKnight *knight) override {
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            int sodu = 0;
            if(level >= levelO){
                level++;
                knight->setlevel(level);
            }
            else{
                if(knight->getKnightType() != 2){
                    // xem có thuốc giải hay không
                    knight->setPo(true);
                    BaseItem *vp = knight->getItem(knight,ANTIDOTE);
                    if(vp == NULL){
                        HP -= 10;
                        knight->setHP(HP);
                        knight->deleteItem(knight);
                    }
                    else vp->use(knight);
                }
            }
        }
};
//7
class Queen : public BaseOpponent{
    public:
        void fight(BaseKnight *knight) override{
            int i = knight->geti();
            int eventid = knight->geteventid();
            int levelO = (i + eventid) % 10 + 1;
            int HP = knight->gethp();
            int level = knight->getlevel();
            int gil = knight->getgil();
            if(level >= levelO){
                gil *= 2;
                knight->setgil(gil);
            }
            else if(level < levelO){
                if(knight->getKnightType() != 0){
                    gil /= 2;
                    knight->setgil(gil);
                }
            }
        }
};
//8
class DeRings : public BaseOpponent{
    public:
        void fight(BaseKnight *knight) override{
            int HP = knight->gethp();
            int level = knight->getlevel();
            int gil = knight->getgil();
            if(gil >= 50){
                if(HP < knight->getmaxhp() / 3){
                    if(knight->getKnightType() == 0){
                        HP += knight->getmaxhp() / 5;
                    }
                    else{
                        gil -= 50;
                        HP += knight->getmaxhp() / 5;
                        knight->setgil(gil);
                        knight->setHP(HP);
                    }
                }
            }
        }
};
//9
class Durian : public BaseOpponent{
    public:
        void fight(BaseKnight *knight) override{
            knight->setHP(knight->getmaxhp());
        }

};
//10
class Omega : public BaseOpponent{
    private:
        bool check;
    public:
        void fight(BaseKnight *knight) override{
            int HP = knight->gethp();
            int level = knight->getlevel();
            int gil = knight->getgil();
            if(level == 10 && HP == knight->getmaxhp() || knight->getKnightType() == 2){
                check = true;
                knight->setlevel(10);
                knight->setgil(999);
            }
            else{
                check = false;
                knight->setHP(0);
            }
        }
        bool defeat(){
            return this->check;
        }
};
//11
class Hades : public BaseOpponent{
    private:
        bool check;
    public:
        void fight(BaseKnight *knight) override{
            int level = knight->getlevel();
            if(level == 10 || knight->getKnightType() == 0 && level >= 8){
                check = true;
            }
            else{
                check = false;
                knight->setHP(0);
            }
        }
        bool defeat(){
            return this->check;
        }

};
/* * * END implementation of class BaseOpponent * * */




/* * * BEGIN implementation of class BaseKnight * * */
bool nt(int HP){
    for(int i = 2;i < HP;i++){
        if(HP % i == 0) return false;
    }
    return HP > 1;
}
bool pytago(int HP){
    if(HP < 100 || HP > 999) {
        return false;
    }
	int a = HP / 100;
	int b = (HP / 10 ) % 10;
	int c = HP  % 10;
    if(a <= 0 || b <= 0 || c <= 0) return false;
    if( (pow(a,2) + pow(b,2)) == pow(c,2) || (pow(c,2) + pow(b,2)) == pow(a,2) || (pow(a,2) + pow(c,2)) == pow(b,2) ) return true;
	return false;
} 
string BaseKnight::toString() const {
    string typeString[4] = {"PALADIN", "LANCELOT", "DRAGON", "NORMAL"};
    // inefficient version, students can change these code
    //      but the format output must be the same
    string s("");
    s += "[Knight:id:" + to_string(id) 
        + ",hp:" + to_string(hp) 
        + ",maxhp:" + to_string(maxhp)
        + ",level:" + to_string(level)
        + ",gil:" + to_string(gil)
        + "," + bag->toString()
        + ",knight_type:" + typeString[knightType]
        + "]";
    return s;
}
class PaladinKnight : public BaseKnight{
    public:
        PaladinKnight(int id, int maxhp, int level, int gil, int antidote, int phoenixdownI){
            this->id = id;
            this->maxhp = maxhp;
            this->hp = maxhp;
            this->level = level;
            this->gil = gil ;
            this->antidote = antidote;
            this->setBag(new PaladinBag(this, phoenixdownI, antidote));
            this->knightType = PALADIN;
        }
};
class LancelotKnight : public BaseKnight{
    public:
        LancelotKnight(int id, int maxhp, int level, int gil, int antidote, int phoenixdownI){
            this->id = id;
            this->maxhp = maxhp;
            this->hp = maxhp;
            this->level = level;
            this->gil = gil ;
            this->antidote = antidote;
            this->setBag(new LancelotBag(this, phoenixdownI, antidote));
            this->knightType = LANCELOT;
        }
};
class DragonKnight : public BaseKnight{
    public:
        DragonKnight(int id, int maxhp, int level, int gil, int antidote, int phoenixdownI){
            this->id = id;
            this->maxhp = maxhp;
            this->hp = maxhp;
            this->level = level;
            this->gil = gil ;
            this->antidote = antidote;
            this->setBag(new DragonBag(this, phoenixdownI, antidote));
            this->knightType = DRAGON;
        }
};
class NormalKnight : public BaseKnight{
    public:
        NormalKnight(int id, int maxhp, int level, int gil, int antidote, int phoenixdownI){
            this->id = id;
            this->maxhp = maxhp;
            this->hp = maxhp;
            this->level = level;
            this->gil = gil ;
            this->antidote = antidote;
            this->setBag(new NormalBag(this, phoenixdownI, antidote));
            this->knightType = NORMAL;
        }
};

//phương thức tạo một đối tượng hiệp sĩ lưu trữ vào mảng động ở class ArmyKnights
BaseKnight * BaseKnight::create(int id, int maxhp, int level, int gil, int antidote, int phoenixdownI){
    // kiểm trả điều kiện maxhp của hiệp sĩ 
    KnightType knightType;
    if(maxhp == 888) knightType = LANCELOT;
    else if(pytago(maxhp)) knightType = DRAGON;
    else if(nt(maxhp)) knightType = PALADIN;
    else knightType = NORMAL;
    

    // tạo đối tượng mới 
    if(knightType == LANCELOT) return new LancelotKnight(id,maxhp,level,gil,antidote,phoenixdownI);
    else if(knightType == DRAGON) return new DragonKnight(id,maxhp,level,gil,antidote,phoenixdownI);
    else if(knightType == PALADIN) return new PaladinKnight(id,maxhp,level,gil,antidote,phoenixdownI);
    return new NormalKnight(id,maxhp,level,gil,antidote,phoenixdownI);
}
/* * * END implementation of class BaseKnight * * */







/* * * BEGIN implementation of class ArmyKnights * * */

// lưu trữ một mãng động chứa các thông tin của hiệp sĩ trong đội quân
ArmyKnights::ArmyKnights (const string & file_armyknights){
    ifstream file; 
    file.open(file_armyknights);
    file >> num_knights;
    demHS = num_knights;
    knights = new BaseKnight*[num_knights];
    for(int i = 0 ;i < num_knights;i++){
        int HP,level,phoenixdownI,gil,antidote;
        knights[i] = new BaseKnight();
        file >> HP >> level >> phoenixdownI >> gil >> antidote;
        knights[i] = BaseKnight::create(i + 1,HP,level,gil,antidote,phoenixdownI);
    }
}
void ArmyKnights::printInfo() const {
    cout << "No. knights: " << this->count();
    if (this->count() > 0) {
        BaseKnight * lknight = lastKnight();
        cout << ";" << lknight->toString();
    }
    cout << ";PaladinShield:" << this->hasPaladinShield()
        << ";LancelotSpear:" << this->hasLancelotSpear()
        << ";GuinevereHair:" << this->hasGuinevereHair()
        << ";ExcaliburSword:" << this->hasExcaliburSword()
        << endl
        << string(50, '-') << endl;
}

void ArmyKnights::printResult(bool win) const {
    cout << (win ? "WIN" : "LOSE") << endl;
}
//giảm đi số lượng hiệp sĩ 
void ArmyKnights::giamHS(){
    num_knights--;
}
//số lượng hiệp sĩ còn lại 
int ArmyKnights::count() const{
    return num_knights;
}
ArmyKnights:: ~ArmyKnights(){
    for (int i = 0; i < num_knights; i++) {
        delete knights[i];
    }
    delete[] knights;
}
bool ArmyKnights::fight(BaseOpponent * opponent){
    BaseKnight *hiepsi = lastKnight();
    opponent->fight(hiepsi);
    if(hiepsi->gethp() <= 0){
        //xem có đủ gil và phoenixdown hay không 
        BaseItem *item = hiepsi->getFirst(hiepsi);
        if(item == NULL){
            if(hiepsi->getgil() >= 100){
                hiepsi->setgil(hiepsi->getgil() - 100);
                hiepsi->setHP(hiepsi->getmaxhp() / 2);
                if(hiepsi->gethp() <= 0) return false;
            }  
            else {
                return false;
            }
        }
        
        else{
            ItemType type = item->getitem();
            BaseItem *use_item = hiepsi->getItem(hiepsi,type);
            use_item->use(hiepsi);
            if(hiepsi->gethp() <= 0){
                if(hiepsi->getgil() >= 100){
                    hiepsi->setgil(hiepsi->getgil() - 100);
                    hiepsi->setHP(hiepsi->getmaxhp() / 2);
                    if(hiepsi->gethp() <= 0) return false;
                }  
                else return false;
            }
        }
    }
    return true;
}

//check điều kiện xem đội quân có đánh bại boss
bool ArmyKnights::adventure(Events *events){
    float HP_BOSS = 5000; // máu của boss
    int defeated10 = 0;
    int defeated11 = 0;

    for(int i = 0; i < events->count() && count() != 0 && demHS != 0 ;i++){
        BaseKnight *hiepsi = lastKnight();
        hiepsi->seti(i);
        hiepsi->seteventid(events->get(i));
        int sodu = 0;//số dư gil
        //gấu MadBear
        if(events->get(i) == 1){
            MadBear *op = new MadBear();
            if(hiepsi->getKnightType() == 0 || hiepsi->getKnightType() == 1){
                hiepsi->setgil(hiepsi->getgil() + 100);
            }
            else{
                if(fight(op) == false){
                    giamHS();
                    demHS--;
                }
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }

        //cướp Bandit
        else if(events->get(i) == 2){
            Bandit *op = new Bandit();
            if(hiepsi->getKnightType() == 0 || hiepsi->getKnightType() == 1){
                hiepsi->setgil(hiepsi->getgil() + 150);
            }
            else{
                if(fight(op) == false){
                    giamHS();
                    demHS--;
                }
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }

        //cướp Lupin
        else if(events->get(i) == 3){
            LordLupin *op = new LordLupin();
            if(hiepsi->getKnightType() == 0 || hiepsi->getKnightType() == 1){
                hiepsi->setgil(hiepsi->getgil() + 450);
            }
            else{
                if(fight(op) == false){
                    giamHS();
                    demHS--;
                }
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }

        //yêu tinh Elf
        else if(events->get(i) == 4){
            Elf *op = new Elf();
            if(hiepsi->getKnightType() == 0 || hiepsi->getKnightType() == 1){
                hiepsi->setgil(hiepsi->getgil() + 750);
            }
            else{
                if(fight(op) == false){
                    giamHS();
                    demHS--;
                }
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }

        //troll
        else if(events->get(i) == 5){
            Troll *op = new Troll();
            if(hiepsi->getKnightType() == 0 || hiepsi->getKnightType() == 1){
                hiepsi->setgil(hiepsi->getgil() + 800);
            }
            else{
                if(fight(op) == false){
                    giamHS();
                    demHS--;
                }
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }   
        else if(events->get(i) == 6){
            Tornbery *op = new Tornbery();
            if(fight(op) == false){
                giamHS();
                demHS--;
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }
        else if(events->get(i) == 7){
            Queen *op = new Queen();
            fight(op);
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }
        else if(events->get(i) == 8){
            DeRings *op = new DeRings();
            fight(op);
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }
        else if(events->get(i) == 9){
            Durian *op = new Durian;
            fight(op);
        }
        else if(events->get(i) == 10){
            if(defeated10 == 0){
                Omega *op = new Omega();
                if(fight(op) == true){
                    defeated10++;
                }
                else{
                    giamHS();
                    demHS--;
                }
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }
        else if(events->get(i) == 11){
            if(defeated11 == 0){
                Hades *op = new Hades();
                if(fight(op) == false){
                    giamHS();
                    demHS--;
                }
                if(op->defeat() == true){
                    set95(true);
                    defeated11++;
                }
                
            }
            BaseItem *item = hiepsi->getFirst(hiepsi);
            if(item != NULL){
                ItemType type = item->getitem();
                BaseItem *use_item = hiepsi->getItem(hiepsi,type);
                use_item->use(hiepsi);
            }
        }
        else if(events->get(i) == 112){
            PhoenixDownII *vp = new PhoenixDownII;
            if(hiepsi->insert(vp,hiepsi) == false){
                for(int i = count() - 2;i >= 0 ; --i ){
                    BaseKnight *next_hiepsi = KnightCount(i);
                    if(next_hiepsi->insert(vp,next_hiepsi)) break;
                }
            }
        }
        else if(events->get(i) == 113){
            PhoenixDownIII *vp = new PhoenixDownIII;
            if(hiepsi->insert(vp,hiepsi) == false){
                for(int i = count() - 2;i >= 0 ; --i ){
                    BaseKnight *next_hiepsi = KnightCount(i);
                    if(next_hiepsi->insert(vp,next_hiepsi)) break;
                }
            }
        }
        else if(events->get(i) == 114){
            PhoenixDownIV *vp = new PhoenixDownIV;
            if(hiepsi->insert(vp,hiepsi) == false){
                for(int i = count() - 2;i >= 0 ; --i ){
                    BaseKnight *next_hiepsi = KnightCount(i);
                    if(next_hiepsi->insert(vp,next_hiepsi)) break;
                }
            }
        }
        else if(events->get(i) == 95){
            set95(true);
        }
        else if(events->get(i) == 96){
            set96(true);
        }
        else if(events->get(i) == 97){
            set97(true);
        }
        else if(events->get(i) == 98){
            if(get95() == true && get96() == true && get97() == true) 
            set98(true);
        }

        // đánh boss
        else if(events->get(i) == 99){
            if(get98() == true) {
                printInfo();
                return true;
            }
            else if(get96() && get97() && get95() && get98() == false){
                if(hiepsi->getKnightType() == 3){
                    demHS--;
                    i--;
                    continue;
                }
                //st paladin
                else if(hiepsi->getKnightType() == 0){
                    float dam = hiepsi->gethp() * hiepsi->getlevel() * 0.05;
                    HP_BOSS -= dam;
                    if(HP_BOSS <= 0){
                        printInfo();
                        return true;
                    }
                    else{
                        giamHS();
                        demHS--;
                        i--;
                        continue;
                    }
                }
                //st lancelot
                else if(hiepsi->getKnightType() == 1){
                    float dam = hiepsi->gethp() * hiepsi->getlevel() * 0.06;
                    HP_BOSS -= dam;
                    if(HP_BOSS <= 0){
                        printInfo();
                        return true;
                    }
                    else{
                        giamHS();
                        demHS--;
                        i--;
                        continue;
                    }

                }
                //st dragon
                else if(hiepsi->getKnightType() == 2){
                    float dam = hiepsi->gethp() * hiepsi->getlevel() * 0.075;
                    HP_BOSS -= dam;
                    if(HP_BOSS <= 0){
                        printInfo();
                        return true;
                    }
                    else{
                        giamHS();
                        demHS--;
                        i--;
                        continue;
                    }
                }
            }
            else{
                break;
            }  
        }
    

        // xem có dư gil hay không
        if(hiepsi->getgil() > 999){
                sodu = hiepsi->getgil() - 999;
                hiepsi->setgil(999);
        }
        //truyền gil cho hiệp sĩ phía trước
        if(sodu != 0){
            for(int index = count() - 2;index >= 0;index--){
                BaseKnight *hiepsi_tien = KnightCount(index);  
                hiepsi_tien->setgil(hiepsi_tien->getgil() + sodu);
                sodu = 0;
                if(hiepsi_tien->getgil() <= 999) break;
                else{
                    sodu = hiepsi_tien->getgil() - 999;
                }
            }
        }
        if(hiepsi->gethp() > hiepsi->getmaxhp()){
            hiepsi->setHP(hiepsi->getmaxhp());
        }
        if(hiepsi->getlevel() > 10){
            hiepsi->setlevel(10);
        }
        if(count() == 0) break;
        printInfo();
    }
    //đội quân thất bại
    num_knights = 0;
    printInfo();
    return false;
}
// trả về đối tượng hiệp sĩ cuối 
BaseKnight * ArmyKnights::lastKnight()const{
    if (demHS == 0) {
        return NULL;
    } else {
        return knights[demHS - 1];
    }
}
BaseKnight * ArmyKnights::KnightCount(int i){
    return knights[i];
};

//check xem báu vật 
bool ArmyKnights::hasPaladinShield() const{
    if(get95()) return true;
    return false;
}
bool ArmyKnights::hasLancelotSpear() const{
    if(get96()) return true;
    return false;
}
bool ArmyKnights::hasGuinevereHair() const{
    if(get97()) return true;
    return false;
}
bool ArmyKnights::hasExcaliburSword() const{
    if(get98()) return true;
    return false;
}
/* * * END implementation of class ArmyKnights * * */



/* * * BEGIN implementation of class KnightAdventure * * */
KnightAdventure::KnightAdventure() {
    armyKnights = nullptr;
    events = nullptr;
}
KnightAdventure::~KnightAdventure(){
    delete armyKnights;
    delete events;
}
//khởi tạo đối tượng ArmyKnights 
void KnightAdventure::loadArmyKnights(const string &file_armyknights){
    armyKnights = new ArmyKnights(file_armyknights);
}
//khởi tạo đối tượng Events
void KnightAdventure::loadEvents(const string &file_events) {
    events = new Events(file_events);
}
void KnightAdventure::run(){
    bool win;
    if(armyKnights->adventure(events)) win = true;
    else win = false; 
    armyKnights->printResult(win);
}
/* * * END implementation of class KnightAdventure * * */