$(() =>{

  const triggerAlert = (message, type) =>{
    toastContainerElem = $("#liveToast")
    toastHeader = $("#liveToast .toast-header strong")
    toastBody = $("#liveToast .toast-body")
    const toastTemplate = `<div  class="toast text-bg-${type}" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <strong class="me-auto">${type}</strong>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      ${message}
    </div>
  </div>`

    toastContainerElem.append(toastTemplate)
    console.log()
    const toast = new bootstrap.Toast($(".toast:last-child"))
    toast.show()

    // toastElem.on('hidden.bs.toast',(e)=>{
    //   toastElem.removeClass(`text-bg-${type}`)
    // })
  }

  $('form#new-note-form').submit((submitEvent)=>{
    submitEvent.preventDefault();
    let formData= $(submitEvent.currentTarget).serialize()
    $.ajax({
      type: "POST",
      url: "/notes",
      data: formData,
      
      success: (response) => {
        $('#notes').html(response)
        $('#note_title')[0].value  = ''
        triggerAlert("Note Added Successfully", "success")
      }
    });
  });

  $('#notes').on('submit', 'form#delete-note', (submitEvent)=>{
    submitEvent.preventDefault();
    let formData = $(submitEvent.currentTarget).serialize()
    $.ajax({
      type: "POST",
      url: "/notes",
      data: formData,
      success: (response) => {
        $('#notes').html(response)
        triggerAlert("Note Deleted Successfully", "danger")
      }
    });
  })

  $('#notes').on('click', 'textarea',(e)=>{
    let textareaElement = $(e.currentTarget)
    textareaElement.prop('readonly',false)
    textareaElement.removeClass('text-bg-light');
    triggerAlert("Editing note Description, press tab or click else where to save", "warning")
  })

  $('#notes').on('focusout', 'textarea', (e)=>{
    // when text area loses focus trigger submit for edit form
    let textareaElement = $(e.currentTarget)
    let formElement = $(textareaElement.parent().closest('form#form#edit-note').prevObject[0])
    textareaElement.prop('readonly',true)
    textareaElement.addClass("text-bg-light")
    formElement.submit()
  })

  $('#notes').on('submit', 'form#edit-note', (submitEvent)=>{
    submitEvent.preventDefault();
    let formElement = $(submitEvent.currentTarget)
    let formData = formElement.serialize()
    $.ajax({
      type: "POST",
      url: "/notes",
      data: formData,
      success: function (response) {
        $('#notes').html(response)
        triggerAlert("Note Description added successfully", "success")
      }
    });
  })
})