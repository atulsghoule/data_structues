//Max_heaps
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
void insert(vector<vector<int>>&heap,vector<int> data);
vector<int> pop(vector<vector<int>>&heap);
void print(vector<vector<int>>&heap);
int main(int argc, const char * argv[]) {
    ifstream cin("/Users/atulkhetan/Desktop/input.txt");
    ofstream cout("/Users/atulkhetan/Desktop/output.txt");
    //[weight,{some_data}]
    vector<vector<int>>heap;
    return 0;
}
//insertion into max_heap
void insert(vector<vector<int>>&heap,vector<int> data){
    heap.push_back(data);
    int parent=(int)(heap.size()-1)/2;
    int child=(int)heap.size()-1;
    vector<int> temp;
    while(parent>-1){
        //need to change here for min or max heap
        if(heap[child][0]>heap[parent][0]){
            temp=heap[parent];
            heap[parent]=heap[child];
            heap[child]=temp;
        }
        else
            return;
        child=parent;
        parent=(parent-1)/2;
    }
}
//pop in max heap
vector<int> pop(vector<vector<int>>&heap){
    vector<int> value=heap[0];
    heap[0]=heap[heap.size()-1];
    heap.pop_back();
    int parent=0;
    int left_child=1;
    int right_child=2;
    vector<int> temp;
    while(parent<(heap.size())/2){
        //need to change here for min heap
        if(heap[parent][0]<heap[left_child][0] && heap[left_child]>heap[right_child]){
            temp=heap[parent];
            heap[parent]=heap[left_child];
            heap[left_child]=temp;
            parent=left_child;
        }
        //need to change here for min heap
        else if(heap[parent][0]<heap[right_child][0]){
            temp=heap[parent];
            heap[parent]=heap[right_child];
            heap[right_child]=temp;
            parent=right_child;
        }
        else
            return value;
        left_child=2*parent+1;
        right_child=2*parent+2;
    }
    return value;
}

