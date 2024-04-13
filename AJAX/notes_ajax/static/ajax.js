$(()=>{
  
  $('form#post-form').submit((e) =>{
    e.preventDefault();
    let formData = $('form#post-form').serialize()
    
    $.ajax({
      url: "/posts",
      type: 'POST',
      data: formData,
      success: (response) => {
        $('#posts').html(response);
        $('textarea').val('')
      }
    });
  })
  $("#posts").on('submit', 'form#delete-form',  (e) => { 
    e.preventDefault();
    console.log(e.currentTarget)
    let formData = $(e.currentTarget).serialize()
    console.log(formData)
    $.ajax({
      type: "POST",
      url: "/posts",
      data: formData,
      success: (response) => {
        $('#posts').html(response);
      }
    });
  });
});