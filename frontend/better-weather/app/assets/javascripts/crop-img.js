// window.cropProfileImage = function(i, pic){
//     var $pic = $(pic);
//     var h = $pic[0].clientHeight,
//         w = $pic[0].clientWidth;

//     if (!$pic[0].currentSrc) {
//       return;
//     }

//     console.log('h w', $pic[0].currentSrc, h, w);

//     if($pic.parent('.image-wrap').length === 0){
//                      // wrap the image in a "cropping" div
//          $pic.wrap('<div class="image-wrap"></div>');
//     }

//       if(h > w ){
//           // pic is portrait
//           $pic.addClass('portrait');
//           var m = -(((h/w) * 100)-100)/2; //math the negative margin
//           $pic.css('margin-top', m + '%');
//       }else if(w > h){
//           // pic is landscape
//           console.log('llll', h, w);
//           var m = -(((w/h) * 100)-100)/2;  //math the negative margin
//           $pic.css('margin-left', m + '%');
//       }else {
//         // pic is square
//         $pic.addClass('square');
//       }
// };

// window.cropImage = function(e) {

//   var imgs = $('.image');
//   var lastImg = imgs[imgs.length - 1];
//   cropProfileImage(lastImg);
// }

// Call the function for the images you want to crop
$(document).ready(function() {
  $('#photos-slides').slick({
    prevArrow: '#prev-photo',
    nextArrow: '#next-photo',
    slidesToShow: 3,
    slidesToScroll: 3
  });

  $('#posts-slides').slick({
    prevArrow: '#prev-post',
    nextArrow: '#next-post',
    slidesToShow: 1,
    slidesToScroll: 1
  });

  // $('.image').each(cropProfileImage); // TODO race condition

  // $('.slides').on('load', 'img', function(e) {
  //   debugger
  // })
});
