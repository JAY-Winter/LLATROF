<template>
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
        caption="">
        <template #img>
          <img
            id="carousel-img"
            class="d-block img-fluid w-100"
            src="https://ifh.cc/g/gdHJRO.png"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

      <!-- <b-carousel-slide
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
      </b-carousel-slide> -->

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
  height: 50vh !important;
  object-fit: cover;
  object-position: top;
}
</style>