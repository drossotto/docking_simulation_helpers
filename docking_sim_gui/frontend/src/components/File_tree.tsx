import React, { useState } from 'react';
import { TreeBeard, TreeNode } from 'react-treebeard';


interface FileTreeProps {
    initialData: TreeNode;
}

const FileTree: React.FC<FileTreeProps> = ({ initialData }) => {
    const [data, setData] = useState<TreeNode>(initialData);
  
    const onToggle = (node: TreeNode, toggled: boolean) => {
      const updateNode = (currentNode: TreeNode): TreeNode => {
        if (currentNode.name === node.name) {
          return { ...currentNode, toggled };
        }
        if (currentNode.children) {
          return {
            ...currentNode,
            children: currentNode.children.map(updateNode),
          };
        }
        return currentNode;
      };
  
      setData(updateNode(data));
    };
  
    return <TreeBeard data={data} onToggle={onToggle} />;
  };
  
  export default FileTree;
