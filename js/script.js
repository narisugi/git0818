<script>
const fruits = ['りんご', 'バナナ', 'みかん', 'ぶどう', 'スイカ', 'パイナップル'];
const spinButton = document.getElementById('spinButton');
const resultElement = document.getElementById('result');
spinButton.addEventListener('click', () => {
  const randomIndex = Math.floor(Math.random() * fruits.length);
  const selectedFruit = fruits[randomIndex];
  resultElement.textContent = `当たり！ ${selectedFruit} が出ました！`;
});
</script>