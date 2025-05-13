function resetForm() {

  const form = document.getElementById('my-form');
  form.reset();

  // 動的に書き換えた部分を手動で初期化（または空にする）  
  form.querySelector('input[name="name"]').value = "";
  form.querySelector('input[name="weight"]').value = "";
  form.querySelector('input[name="sets"]').value = "";
  form.querySelector('input[name="reps"]').value = "";
  form.querySelector('input[name="days"]').value = "";
}
document.getElementById('reset-btn').addEventListener('click', resetForm);