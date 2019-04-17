#include<iostream>
#include<algorithm>
using namespace std;
struct node{
    int data;
    node *next;
};
class graph{
    node *list;
public:
    //intialization of graph
    graph(int v){
        list= new node [v];
        for(int i=0;i<v;i++){
            list[i].data=i+1;
            list[i].next=NULL;
        }
    }
    //finding a edge
    bool find(int v1,int v2){
        node *temp;
        temp=&list[v1-1];
        while(temp){
            if(temp->data==v2)
                return true;
            temp=temp->next;
        }
        return false;
    }
    //insertion of edge
    void insert(int v1,int v2){
        if(!find(v1,v2)){
            node * new_node=new node;
            new_node->next=list[v1-1].next;
            new_node->data=v2;
            list[v1-1].next=new_node;
        }
    }
    //temprory display function
    void display(int v){
        for(int i=0;i<v;i++){
            cout<<list[i].data<<" -> ";
            node *temp=list[i].next;
            while(temp){
                cout<<temp->data<<" ";
                temp=temp->next;
            }
            cout<<endl;
        }
    }
    /*~graph(){
        delete list [];
    }*/
};
int main(){
    graph * new_graph= new graph(4);

    new_graph->insert(1,2);
    new_graph->insert(2,3);
    new_graph->insert(2,4);
    new_graph->insert(3,4);
    new_graph->insert(3,1);
    new_graph->display(4);
    return 0;
}