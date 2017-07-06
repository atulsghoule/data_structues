#include<iostream>
using namespace std;
struct node{
    int data;
    node *left;
    node *right;
};
node *insert(node *root,int data){
    if(root==NULL){
        node *new_node= new node();
        new_node->data=data;
        new_node->left=NULL;
        new_node->right=NULL;
        root=new_node;
    }
    else if(root->data>data)
        root->left=insert(root->left,data);
    else
        root->right=insert(root->right,data);
    return root;
}
bool find(node *root,int data){
    if(root==NULL)
        return false;
    else if(root->data==data)
        return true;
    else if(root->data>data)
        return find(root->left,data);
    else
        return find(root->right,data);
}

void in_order(node *root){
    if(root==NULL)
        return ;
    in_order(root->left);
    cout<<root->data<<" ";
    in_order(root->right);
}
void post_order(node *root){
    
}
int main(){
    node *root=NULL;
    root=insert(root,3);
    root=insert(root,1);
    root=insert(root,5);
    root=insert(root,4);
    root=insert(root,6);
    in_order(root);
    cout<<endl;
    cout<<find(root,6)<<endl;
    return 0;
}