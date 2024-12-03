<template>
  <footer class="main-footer">
    <div class="footer-content">
      <div class="footer-left">
        <p>© 2024 FinPick. All rights reserved.</p>
      </div>
      <div class="footer-links">
        <RouterLink to="/" class="footer-link">About Us</RouterLink>
        <RouterLink to="/" class="footer-link">Privacy Policy</RouterLink>
        <RouterLink to="/" class="footer-link">Terms of Service</RouterLink>
        <RouterLink to="/" class="footer-link">FAQ</RouterLink>
      </div>
      <div class="footer-social">
        <a href="https://facebook.com" class="social-icon facebook" target="_blank" rel="noopener noreferrer"></a>
        <a href="https://twitter.com" class="social-icon twitter" target="_blank" rel="noopener noreferrer"></a>
        <a href="https://instagram.com" class="social-icon instagram" target="_blank" rel="noopener noreferrer"></a>
      </div>
    </div>
  </footer>
</template>

<script setup>
// Vue composition API 사용 예시
</script>

<style scoped>
.page-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh; 
}

main {
  flex-grow: 1; /* 콘텐츠 영역이 남은 공간을 차지하도록 설정 */
}

.main-footer {
  background-color: #f9f9fc; /* 부드러운 흰색 배경 */
  color: #333; /* 텍스트를 가독성 있는 회색으로 */
  padding: 3rem 0;
  border-top: 1px solid #eaeaea; /* 상단 경계선을 추가 */
  text-align: center; /* 중앙 정렬 */
  margin-top: 7rem; /* 경계선 위에 여백 추가 */
}

.footer-content {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column; /* 세로 배치 */
  gap: 1rem; /* 항목 간격 추가 */
  align-items: center;
}

.footer-left {
  font-size: 0.9rem; /* 작게 조정 */
  color: #666; /* 회색으로 부드럽게 */
}

.footer-links {
  display: flex;
  gap: 1.5rem; /* 링크 간격 확장 */
}

.footer-link {
  color: black;
  text-decoration: none;
  font-size: 0.9rem; /* 크기 조정 */
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: #0056b3; /* 어두운 파란색으로 강조 */
}

.footer-social {
  display: flex;
  gap: 1.5rem; /* 아이콘 간격 확장 */
}

.social-icon {
  width: 38px; /* 아이콘 크기 */
  height: 38px;
  display: inline-block;
  background-size: cover; /* 이미지를 요소 크기에 맞춤 */
  background-repeat: no-repeat;
  transition: transform 0.3s ease; /* 호버 시 효과 */
}

.social-icon.facebook {
  background-image: url('@/assets/image/facebook.png');
}

.social-icon.twitter {
  background-image: url('@/assets/image/twitter.png');
}

.social-icon.instagram {
  background-image: url('@/assets/image/instagram.png');
}

.social-icon:hover {
  transform: scale(1.1); /* 호버 시 크기 확대 */
}
</style>