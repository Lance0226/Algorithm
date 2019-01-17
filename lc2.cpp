/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       
        return addTwo(l1,l2,0);
    }
    
private:
    ListNode* addTwo(ListNode* l1, ListNode* l2, int isPlus)
    {
        int l1Val = l1 ? l1->  val : 0;
        
        int l2Val = l2 ? l2 -> val : 0;
        
        int val = l1Val + l2Val + isPlus;
        
        ListNode *ans = new ListNode(val % 10);
        
        int nextPlus = val >= 10 ? 1 : 0 ;
        
        ListNode *l1Next = l1 ? l1->next : l1;
        
        ListNode *l2Next = l2 ? l2->next : l2;
        
        if (l1Next || l2Next || nextPlus ) {
            
            ans->next = addTwo(l1Next, l2Next, nextPlus);
        }
        
        return ans;
    }
    
    
};