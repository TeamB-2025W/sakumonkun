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

const updateQuestionForm = document.getElementById('update_question_form');

// 編集ボタンの動作
function showEditForm(blockId) {
    const block = document.getElementById(blockId);
    const viewMode = block.querySelector('.view_mode');
    const editMode = block.querySelector('.edit_mode');
      
    viewMode.style.display = 'none';
    editMode.style.display = 'block';
}

// 保存ボタンの動作
function saveEdit(blockId) {
    const block = document.getElementById(blockId);
    const viewMode = block.querySelector('.view_mode');
    const editMode = block.querySelector('.edit_mode');
    
    updateQuestionForm.submit();
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

let currentBlockId = '';// ブロックidを格納する変数を作成
const body = document.body;
let scrollPosition = 0;

// id毎の削除モーダルを表示
function showDeleteConfirmation(blockId) {
    scrollPosition = window.pageYOffset;
    body.style.top = `-${scrollPosition}px`;
    body.classList.add('no-scroll');
    currentBlockId = blockId;
    document.getElementById(`deleteConfirmationModal_${currentBlockId}`).style.display = 'block';
}

// 削除モーダルを閉じる処理
function closeModal(blockId) {
    body.classList.remove('no-scroll');
    body.style.top = '';
    window.scrollTo(0, scrollPosition);
    document.getElementById(`deleteConfirmationModal_${currentBlockId}`).style.display = 'none';
}

// ブロック削除処理＆DB削除処理
function deleteBlock(blockId) {
    document.getElementById(`delete_${blockId}`).submit();
}

// モーダル外クリックでモーダルを閉じる
window.onclick = function(event) {
    if (event.target == document.getElementById('deleteConfirmationModal')) {
        closeModal();
    }
}