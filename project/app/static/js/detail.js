"use strict";

// URLcopybox

const urlInput = document.querySelector('.url_get');
const copyButton = document.querySelector('.copy_button');

copyButton.addEventListener('click', () => {
    urlInput.select();
    navigator.clipboard.writeText(urlInput.value).then(() => {
        copyButton.textContent = 'Copied!';
        copyButton.classList.add('copied');
        setTimeout(() => {
            copyButton.textContent = 'Copy';
            copyButton.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
});




//編集・削除ボタンの挙動

// ブロックidを格納する変数を作成
let currentBlockId = '';

// 編集ボタンの動作
function showEditForm(blockId) {
    const block = document.getElementById(blockId);
    const viewMode = block.querySelector('.view_mode');
    const editMode = block.querySelector('.edit_mode');
    const content = block.querySelector('.view_content');//編集前の内容を格納
            
    viewMode.style.display = 'none';
    editMode.style.display = 'block';
    editMode.querySelector('.edit_content') = content;//編集前の内容を編集画面に表示
}

// 保存ボタンの動作
function saveEdit(blockId) {
    const block = document.getElementById(blockId);
    const viewMode = block.querySelector('.view_mode');
    const editMode = block.querySelector('.edit_mode');
    const newContent = editForm.querySelector('.edit_content');//編集後の内容を格納
    
    block.querySelector('.view-content') = newContent;//編集後の内容を表示
    viewMode.style.display = 'block';
    editMode.style.display = 'none';
}

// 編集をキャンセルして閲覧モードに戻る
function cancelEdit(blockId) {
    const block = document.getElementById(blockId);
    const viewMode = block.querySelector('.view_mode');
    const editForm = block.querySelector('.edit_mode');
    
    viewMode.style.display = 'block';
    editForm.style.display = 'none';
}

const body = document.body;
let scrollPosition = 0;

// id毎の削除モーダルを表示
function showDeleteConfirmation(blockId) {
    scrollPosition = window.pageYOffset;
    body.style.top = `-${scrollPosition}px`;
    body.classList.add('no-scroll');
    currentBlockId = blockId;
    document.getElementById('deleteConfirmationModal').style.display = 'block';
}

// 削除モーダルを閉じる処理
function closeModal() {
    body.classList.remove('no-scroll');
    body.style.top = '';
    window.scrollTo(0, scrollPosition);
    document.getElementById('deleteConfirmationModal').style.display = 'none';
}

// ブロック削除処理＆DB削除処理
function deleteBlock() {
    if (currentBlockId) {
        const blockElement = document.getElementById(currentBlockId);
        if (blockElement) {
            blockElement.remove();
        }
    }
    closeModal();
}

// モーダル外クリックでモーダルを閉じる
window.onclick = function(event) {
    if (event.target == document.getElementById('deleteConfirmationModal')) {
        closeModal();
    }
}