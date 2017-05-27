#include<iostream>
using namespace std;
class list
{
    struct node
    {
        int key;
        node *next;
        node *prev;
    };
    public:
    node *root;
    list()
    {
        root=NULL;
        
    }
    node *list_search(int value)
    {
        node *temp=root;
        while(temp!=NULL && temp->key!=value)
            temp=temp->next;
        return temp;
    }
    void list_insert(int value)
    {
        node *new_node=new node();
        new_node->key=value;
        if(root==NULL)
        {
            root=new_node;
            new_node->next=NULL;
            new_node->prev=NULL;
        }
        else
        {
            new_node->next=root->next;
            root->next=new_node;
            new_node->prev=root;
        }
    }
    void list_delete(int key)
    {
        node *to_delete=list_search(key);
        if(to_delete==NULL)
        {
            cout<<"False value\n";
            return;
        }
        if(to_delete->prev!=NULL)
            (to_delete->prev)->next=to_delete->prev;
        else
            root=to_delete->next;
        if(to_delete->next!=NULL)
            (to_delete->next)->prev=to_delete->prev;
        delete to_delete;
    }
    void print()
    {
        node *temp=root;
        while(temp!=NULL)
        {
            cout<<temp->key<<" ";
            temp=temp->next;
        }
    }
};
