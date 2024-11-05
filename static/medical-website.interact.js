jQuery(document).ready(function(){
    jQuery(document).on("submit", "#user_input", function(){
        event.preventDefault();

        let user_first_name = jQuery('#first_name').val();
        let user_last_name = jQuery('#last_name').val();
        let user_age = jQuery('#age').val();
        let user_gender;
        if(document.getElementById("male").checked){
            user_gender = "male";
        } else if(document.getElementById("female").checked){
            user_gender = "female";
        } else{
            user_gender = "other";
        }
        let user_height_ft = jQuery('#height_ft').val();
        user_height_ft = parseInt(user_height_ft, 10);
        let user_height_in = jQuery('#height_in').val();
        user_height_in = parseInt(user_height_in, 10);
        let user_weight = jQuery('#weight').val();
        user_weight = parseFloat(user_weight);
        let user_race = jQuery('#race').val();
        let user_disease = jQuery('#disease').val()
        let user_consent
        if(jQuery('#consent-checkbox').length > 0) {
            user_consent = jQuery('#consent-checkbox').prop('checked');
        } else {
            user_consent = 0;
        }
        if(user_first_name && user_last_name && user_age && user_gender && user_height_ft && user_height_in && user_weight && user_race) {
            $.ajax({
                url: '/submit',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    first_name: user_first_name,
                    last_name: user_last_name,
                    age: user_age,
                    gender: user_gender,
                    height_ft: user_height_ft,
                    height_in: user_height_in,
                    weight: user_weight,
                    race: user_race,
                    disease: user_disease,
                    consent: user_consent
                }),
                success: function(response){
                    alert('Data submit successfully: ' + JSON.stringify(response));
                },
                error: function(){
                    alert('Error submitting data: ');
                }
            });
        } else {
            alert('Incorrect Input!');
        }
    })

    jQuery('#disease').on('change', function(){
        let selectedValue = jQuery(this).val();
        if(selectedValue !== "None"){
            if(jQuery('#consent-checkbox').length == 0){
                jQuery('#consent').append (
                    '<input type="checkbox" id="consent-checkbox" style="flex 0 0 auto;"/>' +
                    '<label for="consent-checkbox" style="flex 1; text-align: left;">' +
                        'I consent to have the information I provided added to the MTSU Center for Medical Database Management and Research database.' +
                    '</label>'
                )
            }
        } else{
            jQuery('#consent').empty();
        }
    })
})