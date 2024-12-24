import * as vscode from 'vscode';

function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.insertDate', () => {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const date = new Date().toLocaleString('ru-RU', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            });
            
            editor.edit((editBuilder: vscode.TextEditorEdit) => {
                editBuilder.insert(editor.selection.active, date);
            });
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}

export { activate };