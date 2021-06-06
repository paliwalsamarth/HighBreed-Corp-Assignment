  var mytoastMixin = Swal.mixin({
    toast: true,
    icon: 'success',
    title: 'General Title',
    position: 'bottom',
    showConfirmButton: false,
    timer: 2000,
    timerProgressBar: true,
    // didOpen: (toast) => {
    //   toast.addEventListener('mouseenter', Swal.stopTimer)
    //   toast.addEventListener('mouseleave', Swal.resumeTimer)
    // }
  });


function mytoaster(title,icon){
    
        mytoastMixin.fire({
          title: title,
          icon: icon,


        });
};


// var toastMixin = Swal.mixin({
//     toast: true,
//     icon: 'success',
//     title: 'General Title',
//     animation: false,
//     position: 'top-right',
//     showConfirmButton: false,
//     timer: 3000,
//     timerProgressBar: true,
//     didOpen: (toast) => {
//       toast.addEventListener('mouseenter', Swal.stopTimer)
//       toast.addEventListener('mouseleave', Swal.resumeTimer)
//     }
//   });