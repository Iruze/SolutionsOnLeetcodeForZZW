/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        if(root == null)
            return list;
        
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);
        int curLay = 1;
        int nextLay = 0;
        
        List<Integer> curList = new ArrayList<>();
        while(!deque.isEmpty())
        {
            TreeNode node = deque.pop();
            curList.add(node.val);
            curLay--;
            
            if(node.left != null) {
                deque.add(node.left);
                nextLay++;
            }
            if(node.right != null) {
                deque.add(node.right);
                nextLay++;
            }
            
            if(curLay == 0)
            {
                curLay = nextLay;
                nextLay = 0;
                list.add(curList);
                curList = new ArrayList<>();
            }
        }
        
        return list;
    }
}
