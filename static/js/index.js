// * ScollReveal effect
// Common reveal options to create reveal animations
ScrollReveal({
  //   reset: true,
  distance: "60px",
  duration: 1250,
  delay: 200,
});

// Target elements and specify options to create reveal animations
ScrollReveal().reveal(".serene-main-title, .serene-section-title", {
  delay: 250,
  origin: "left",
});
ScrollReveal().reveal(".sec-01 .serene-image, .serene-info", {
  delay: 300,
  origin: "bottom",
});
ScrollReveal().reveal(".serene-text-box", {
  delay: 350,
  origin: "right",
});
ScrollReveal().reveal(".serene-media-icons i", {
  delay: 250,
  origin: "bottom",
  interval: 100,
});
ScrollReveal().reveal(".sec-02 .serene-image, .sec-03 .serene-image", {
  delay: 250,
  origin: "top",
});
ScrollReveal().reveal(".serene-media-info li", {
  delay: 250,
  origin: "left",
  interval: 100,
});
