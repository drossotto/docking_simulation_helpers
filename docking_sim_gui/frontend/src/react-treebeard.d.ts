declare module 'react-treebeard' {
    import * as React from 'react';

    export interface TreeNode {
        name: string;
        toggled?: boolean;
        children?: TreeNode[];
    }

    export interface TreeBeardProps {
        data: TreeNode;
        onToggle?: (node: TreeNode, toggled: boolean) => void;
    }

    export class TreeBeard extends React.Component<TreeBeardProps> {}
}