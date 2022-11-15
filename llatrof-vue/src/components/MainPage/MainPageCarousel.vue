<template>
<!-- <div class="carousel slide carousel-fade position-relative" data-bs-ride="carousel" data-bs-touch="true">
  <div class="carousel-inner">
    <div class="carousel-item active" data-bs-interval="2100">
      <img src="https://pbs.twimg.com/media/DLvkgHvU8AA5bzt.jpg" class="d-block w-100" alt="#" id="carousel-img">
    </div>
    <div class="carousel-item">
      <img src="http://cdnimage.dailian.co.kr/news/202112/news_1639226193_1062178_m_1.jpeg" class="d-block w-100" alt="#" id="carousel-img">
    </div>
    <div class="carousel-item">
      <img src="http://image.cine21.com/resize/cine21/person/2008/1027/P0000019_dvd67606[W578-].jpg" class="d-block w-100" alt="#" id="carousel-img">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div> -->

<!-- bootstrapview를 사용함 -->
  <div>
    <b-carousel
      id="carousel-fade"
      style="text-shadow: 0px 0px 2px #000"
      fade
      controls
      label-next=""
      label-prev=""
      indicators
    >
      <b-carousel-slide
        caption="First slide">
        <template #img>
          <img
            id="carousel-img"
            class="d-block img-fluid w-100"
            src="https://pbs.twimg.com/media/DLvkgHvU8AA5bzt.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

      <b-carousel-slide
        caption="Second slide">
        <template #img>
          <img
            id="carousel-img"
            class="d-block img-fluid w-100"
            src="https://media.gq.com/photos/5e6128d2398289000862596e/master/pass/tom-hardy-lead-840-social.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

      <b-carousel-slide
        caption="Thrid slide">
        <template #img>
          <img
            id="carousel-img"
            class="d-block img-fluid w-100"
            src="https://hips.hearstapps.com/esquireuk.cdnds.net/15/37/original/original-tom-hardy-esquire-may-cover-promo-11-jpg-4c8bc653.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

    </b-carousel>
  </div>
</template>

<script>
export default {
}
</script>

<style>
#carousel-fade {
  margin-bottom: 0.5rem;
}
#carousel-fade {
  align-content: center;
}
#carousel-img {
  height: 50vw !important;
  object-fit: cover;
  object-position: top;
  border-radius: 10px;
}
</style>