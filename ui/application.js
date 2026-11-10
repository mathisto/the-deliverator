// Native markup adapter. It never dispatches actions, replaces controls or owns engine state.
const apply = root => {
  const buttons = root.matches?.('button') ? [root] : [...(root.querySelectorAll?.('button') || [])];
  for (const button of buttons) {
    if(button.closest('[data-dv-preserve]'))continue;
    button.classList.add('dv-button');
  }
};
apply(document);
new MutationObserver(records=>records.forEach(record=>record.addedNodes.forEach(node=>{if(node.nodeType===1)apply(node)}))).observe(document.body,{childList:true,subtree:true});
