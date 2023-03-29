
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        vector<int> ans;
        vector<bool> visited(V+1,false);
        queue<int> q;
        int s=0;
        q.push(s);
        while(!q.empty())
        {
            int m=q.front();
            q.pop();
            ans.push_back(m);
            visited[m]=true;
            for(auto it:adj[m])
            {
                if(visited[it]==false)
                {
                    q.push(it);
                    visited[it]=true;
                }
            }
        }
        return ans;
    }
};

