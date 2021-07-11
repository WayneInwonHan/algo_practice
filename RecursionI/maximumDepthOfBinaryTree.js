var maxDepth = function(root) {
    var bl=function(node){
        var max=0;
        if(node!=null){
            max++;
            var ml=bl(node.left);
            var mr=bl(node.right);
            max+=ml>mr?ml:mr;        
        }
        return max;
    }
    var dd=bl(root);
    return dd;
};