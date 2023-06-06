#include<iostream>
#include<unordered_map>
#include<list>



using namespace std;
template <   typename T>


class graph{
 
public:
    unordered_map<T, list<T>> adj;
     
     void addEdge(T u, T v,bool direction ) {   // u and v for nodes u and v 
      // direction =0 -> undirected
      //dirdction =1 ->directed
    
    //create an edge from u to v
      adj[u].push_back(v);     //joining from u to v
        
        if(direction ==0)     // if it is undirected
{
    adj[v].push_back(u);   //then join from v to u ALSO
     
}


     }

void printadj(){

for(auto i:adj){
    cout << i.first << "->";
    for(auto j:i.second){

        cout << j << ",";

    }

    cout << endl;
}



}




};

int main(){

int n;
cout << "enter edge no " << endl;
cin >> n;

int m;
cout << "enter node  no " << endl;
cin >> m;

graph g;

for (int i = 0; i < m;i++){
int u, v;

cin >> u >> v;
g.addEdge(u, v, 0); // creating an undirected graph
}

g.printadj();

return 0;
}