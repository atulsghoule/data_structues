#include<iostream>
using namespace std;
class linked_list
{
    struct node
    {
        int data;
        node* next;
        node* prev;
    };
    node *root;
public:
    linked_list()
    {
        root=new node;
        root->data=0;
        root->next=NULL;
        root->prev=NULL;
    }
    void list_insert(int num)
    {
        node *new_node=new node;
        new_node->data=num;
        if(root->next!=NULL)
        {
            new_node->next=root->next;
            (root->next)->prev=new_node;
            root->next=new_node;
            new_node->prev=root;
        }
        else
        {
            new_node->prev=root;
            new_node->next=NULL;
            root->next=new_node;
        }
    }
    node* list_find(int num)
    {
        node* search=root;
        while(search!=NULL)
        {
            if(search->data==num)
                return search;
            search=search->next;
        }
        return NULL;
    }
    bool list_delete(int num)
    {
        node* search=list_find(num);
        if(search==NULL||search==root)
            return false;
        else if(search->next==NULL)
        {
            (search->prev)->next=NULL;
            delete search;
            return true;
        }
        (search->next)->prev=search->prev;
        (search->prev)->next=search->next;
        delete search;
        return true;
    }
    void display()
    {
        cout<<"\n";
        node* pr=root;
        while(pr!=NULL)
        {
            cout<<" "<<pr->data<<" ";
            pr=pr->next;
        }
        cout<<"\n\n";
    }
    void buff()
    {
        cout<<"-----------------------------------------------\n";
    }
    ~linked_list()
    {
        delete root;
    }
};
int main()
{
    linked_list *list =new linked_list();
    int num,op;
    while(true)
    {
        cout<<"\n Insert - 1\n Delete - 2\n Find - 3\n Anyother - Exit\n";
        cout<<"\n Enter option : ";
        cin>>op;
        if(op==1)
        {
            cout<<" Enter a number : ";
            cin>>num;
            list->list_insert(num);
            list->buff();
            cout<<" Data Inserted\n";
        }
        else if(op==2)
        {
            cout<<" Enter a number : ";
            cin>>num;
            if(list->list_delete(num)==false)
            {
                list->buff();
                cout<<" Not found\n";
            }
            else
            {
                list->buff();
                cout<<" Data deleted\n";
            }
        }
        else if(op==3)
        {
            cout<<" Enter a number : ";
            cin>>num;
            if(list->list_find(num)==NULL)
            {
                list->buff();
                cout<<" Dose not exist\n";
            }
            else
            {
                list->buff();
                cout<<" Exist\n";
            }
        }
        else
            break;
        list->buff();
    }
    list->display();
    delete list;
    return 0;
}