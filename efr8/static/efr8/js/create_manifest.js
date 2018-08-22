function create_liner_manifest(){
    debugger
    var data = {
        destination_port: $('#destination_port').val(),
        vessel: $('#vessel').val(),
        eta_date: $('#eta_date').val(),
        eta_time: $('#eta_time').val(),
        container_number: $('#container_number').val(),
        container_size: $('#container_size').val(),
        container_type: $('#container_type').val(),
        delivery_type: $('#delivery_type').val(),
        transporter: $('#transporter').val(),
        icd_cfs: $('#icd_cfs').val()
    }
    $.ajax({
        type: 'POST',
        url: '',
        data: data,
        dataType: 'json',
        success: function(data) {
            window.location.href = '/liner/'
        },
        error:function(data, error){
          console.log(error)
        }        
    });
    return false
}