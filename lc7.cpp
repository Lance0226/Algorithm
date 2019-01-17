class Solution
{
public:
        int reverse(long x)
    {
           
        int flag;
        
        if (x>0)
        {
            flag = 1;
        }
        else
        {
            flag = -1;
            
            x = -x;
        }
        
        
        string s1 = to_string(x);
        
        stack<int> q;
        
        for (char&c : s1)
        {
            q.push(c);
        }
        
        int is_head = 0;
        string s2 = "";
        
        while (!q.empty())
        {
            char p = q.top();
            q.pop();
            
            if (is_head == 0)
            {
                if (p != 0)
                {
                    s2 += p;
                    is_head = 1;
                }
            }
            else
            {
                s2 += p;
            }
        }
       
  
        
        int y = 0;
        
        try {
            y= stoi(s2);
        } catch (out_of_range& e) {
            return 0;
        }
        
      
        
        int result = y * flag;
        
        return result;
        
        
    }
};
