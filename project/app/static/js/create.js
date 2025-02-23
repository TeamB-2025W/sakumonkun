"use strict";

const addQuestionButton = document.getElementById("addQuestionButton");
const removeQuestionButton = document.getElementById("removeQuestionButton");

addQuestionButton.addEventListener("click", () => {
  addQuestionForm();
  // 連打防止のため1秒無効化
  disableButton(addQuestionButton);
  setTimeout(() => {
    enableButton(addQuestionButton);
  }, 1000);
});

removeQuestionButton.addEventListener("click", () => {
  removeQuestionForm();
  disableButton(removeQuestionButton);
  setTimeout(() => {
    enableButton(removeQuestionButton);
  }, 1000);
})

function addQuestionForm() {
  // 要素を作成・属性の設定

  // 親要素
  const questions = document.getElementById("questions");
  // 追加するまとめ要素
  const question = document.createElement("li");
  question.classList.add("question");
  // タイトル
  const title = document.createElement("h3");
  title.textContent = `問題 ${questions.children.length + 1}`;
  // 問題文の入力欄
  const questionText = document.createElement("textarea");
  questionText.placeholder = "問題文";
  questionText.rows = 5;
  questionText.cols = 96;
  // 選択肢ラベル
  const choicesLabel = document.createElement("label");
  choicesLabel.className = "flex choiceies";
  choicesLabel.innerHTML = "<p>選択肢</p><p>正答</p>";
  // 選択肢リスト
  const choicesList = document.createElement("ol");
  choicesList.className = "choiceies";
  // 4つの選択肢を作成・追加
  for (let i=0; i<4; i++) {
    const choiceItem = document.createElement("li");
    choiceItem.className = "flex";

    const choiceLabel = document.createElement("label");
    choiceLabel.textContent = i + 1;

    const choiceInput = document.createElement("input");

    const choiceRadio = document.createElement("input");
    choiceRadio.type = "radio";
    choiceRadio.name = `correct-${questions.children.length + 1}`;

    // 要素を連結
    choiceItem.appendChild(choiceLabel);
    choiceItem.appendChild(choiceInput);
    choiceItem.appendChild(choiceRadio);
    choicesList.appendChild(choiceItem);
  }
  // 解説ラベル
  const commentaryLabel = document.createElement("label");
  commentaryLabel.setAttribute("for", `commentary-${questions.children.length + 1}`);
  commentaryLabel.className = "commentary";
  commentaryLabel.textContent = "解説";
  // 解説の入力欄
  const commentaryText = document.createElement("textarea");
  commentaryText.className = "commentary";
  commentaryText.id = `commentary-${questions.children.length + 1}`;
  commentaryText.placeholder = "解説文";
  commentaryText.rows = 7;
  commentaryText.cols = 96;

  // 要素を連結
  question.appendChild(title);
  question.appendChild(questionText);
  question.appendChild(choicesLabel);
  question.appendChild(choicesList);
  question.appendChild(commentaryLabel);
  question.appendChild(commentaryText);
  questions.appendChild(question);
}

function disableButton(addQuestionButton) {
  addQuestionButton.disabled = true;
  addQuestionButton.style.background = "gray";
}

function enableButton(addQuestionButton) {
  addQuestionButton.disabled = false;
  addQuestionButton.style.background = "#00bfff";
}
// 一つ目は除いて最後の要素を削除する
function removeQuestionForm() {
  // 親要素
  const questions = document.getElementById("questions");
  const lastIndex = questions.children.length - 1;
  if (lastIndex < 1) return;
  const removeQuestion = questions.children[lastIndex];
  questions.removeChild(removeQuestion);
}