$(document).ready(function(){
checkedToggles = [];

// set the Showing X text on page load
$('.cp-ability-count__toggle').text($('.ability').length)
$('.cp-ability-count__total').text($('.ability').length)

// on click, edit the arrays and loop through them.
$('.cp-ability-controls__dropdown li input').on('click', function() {
    checkedToggles = [];
    // depending on what's clicked, change the text of the dropdown filters.
    if ($(this).parents('.cp-ability-controls__dropdown--actionType').length) {
        toggle = $(this).siblings('label').html()
        if (toggle == 'All') {toggle = 'Action Type'}
        $(this).parents('fieldset').children('legend').text(toggle)
    } else if ($(this).parents('.cp-ability-controls__dropdown--recharge').length) {
        toggle = $(this).siblings('label').html()
        if (toggle == 'All') {toggle = 'Recharge'}
        $(this).parents('fieldset').children('legend').text(toggle)
    } else if ($(this).parents('.cp-ability-controls__dropdown--keyword').length) {
        toggle = $('.cp-ability-controls__dropdown--keyword input:checked').length
        if (toggle == 0) {keywords = 'Keyword'}
        if (toggle == 1) {keywords = '1 Keyword'}
        if (toggle > 1) {keywords = toggle+' Keywords'}
        $(this).parents('fieldset').children('legend').text(keywords)
    }
    // loop through the action types and add active to array.
    $('.cp-ability-controls__dropdown--actionType li input').each(function(){
        if ($(this).is(':checked') && $(this).data('toggle') !== 'all') {
            toggle = $(this).data('toggle')
            checkedToggles.push(toggle);
        }
    })
    // loop through the recharge and add active to array.
    $('.cp-ability-controls__dropdown--recharge li input').each(function(){
        if ($(this).is(':checked') && $(this).data('toggle') !== 'all') {
            toggle = $(this).data('toggle')
            checkedToggles.push(toggle);
        }
    })
    // loop through the keywords and add active to array.
    $('.cp-ability-controls__dropdown--keyword li input').each(function(){
        if ($(this).prop('checked') && $(this).data('toggle') !== 'all') {
            toggle = $(this).data('toggle')
            checkedToggles.push(toggle);
        }
    })
    // Now show/hide the abilities based on the array entries
    if (checkedToggles == '') {
        $('.ability').removeClass('hide');
        $('.cp-ability-count__toggle').text($('.ability:not(.hide):not(.used)').length)
    } else {
        setAbilities(checkedToggles);
    }
})
    
function setAbilities(checkedToggles) {
    $('.ability').each(function(){
        row = $(this).data("compare");
        var rowArr = row.split(",");
        for(var i = 0; i < checkedToggles.length; i++){
            // indexOf returns -1 when no match
            if ((rowArr.indexOf(checkedToggles[i]) == -1)) {
                $(this).addClass('hide');
                break;
            } else {
                 $(this).removeClass('hide');
            }
        }
    });
    $('.cp-ability-count__toggle').text($('.ability:not(.hide):not(.used)').length)
}    

// show/hide dropdowns on click
$('.cp-ability-controls__dropdown legend').on('click', function() {
    if ($(this).parent().parent().hasClass('active')) {
        $('.cp-ability-controls__dropdown').removeClass('active')
    } else {
        $('.cp-ability-controls__dropdown').removeClass('active')
        $(this).parent().parent().addClass('active')
    }
})

// attack workspace calculations
$('.cp-attack-workspace__ability-scores-select').on('change', function(){
    weapon = $(this).data('type')
    abilitySelected = $(this).val()
    calcWorkspace(abilitySelected,weapon)
    console.log(weapon)
})

// add a border to clicked elements and calc workspace
$('.ability').on('click', function() {
$('.ability').removeClass('clicked')
    $(this).toggleClass('clicked')
    abilitySelected = $(this).data('attack-stat').substr(0,3)
    if (abilitySelected !== '') {
        calcWorkspace(abilitySelected,'both')
    }
})

// show/hide tabs when clicked
$('.cp-attack-workspace__tab').on('click', function() {
    target = $(this).parent().toggleClass('open')
})

// show/hide abilities when used
$('.ability-used input').on('click', function() {
    target = $(this).parents('.ability').addClass('used')
    $('.cp-ability-count__toggle').text($('.ability:not(.hide):not(.used)').length)

})

// ability reset
$('.cp-ability-controls__controls-reset button').on('click', function() {
    $('.ability').removeClass('used')
    $('.ability-used input').prop('checked', false)
    $('#actiontype-all--toggle').prop('checked', 'checked')
    $('#recharge-all--toggle').prop('checked', 'checked')
    $('.cp-ability-controls__dropdown--keyword li').each(function() {
        if ($(this).find('input').prop('checked')) {
            $(this).find('input').prop('checked', false)
        }
    })
    $('.cp-ability-controls__dropdown--actionType').find('legend').text('Action Type')
    $('.cp-ability-controls__dropdown--recharge').find('legend').text('Recharge')
    $('.cp-ability-controls__dropdown--keyword').find('legend').text('Keyword')
    $('.ability').removeClass('hide');
    $('.cp-ability-count__toggle').text($('.ability:not(.hide):not(.used)').length)

})

$('.cp-ability-controls__menu-toggle').on('click', function() {
    $('body').toggleClass('controls-open')
})

function calcWorkspace(modifier,weapon) {
    modifier = modifier.toUpperCase();
    modValue = $('.cp-attack-workspace__ability-scores .'+modifier+' .mod').text()
    if (weapon == 'primary') {
        $('.primary-attack-workspace .ability-bonus').text(modValue)
    } else if (weapon == 'secondary') {
        $('.secondary-attack-workspace .ability-bonus').text(modValue)
    } else if (weapon == 'extra') {
        $('.extra-attack-workspace .ability-bonus').text(modValue)
    } else {
        $('.primary-attack-workspace .ability-bonus').text(modValue)
        $('.secondary-attack-workspace .ability-bonus').text(modValue)
        $('.extra-attack-workspace .ability-bonus').text(modValue)
    }
    primaryTotal = 0;
    secondaryTotal = 0;
    extraTotal = 0;
    $('.primary-attack-workspace .bonus').each(function() {
        primaryTotal = primaryTotal + parseInt($(this).text());
    })
    $('.secondary-attack-workspace .bonus').each(function() {
        secondaryTotal = secondaryTotal + parseInt($(this).text());
    })
    $('.extra-attack-workspace .bonus').each(function() {
        extraTotal = extraTotal + parseInt($(this).text());
    })
    $('.primary-attack-workspace .total-bonus').text(primaryTotal)
    $('.secondary-attack-workspace .total-bonus').text(secondaryTotal)
    $('.extra-attack-workspace .total-bonus').text(extraTotal)
    if (weapon == 'primary') {
        $('.cp-attack-workspace__ability-scores-select--primary').val(modifier)  
    } else if (weapon == 'secondary') {
        $('.cp-attack-workspace__ability-scores-select--secondary').val(modifier)  
    } else if (weapon == 'extra') {
        $('.cp-attack-workspace__ability-scores-select--extra').val(modifier)  
    } else {
        $('.cp-attack-workspace__ability-scores-select--primary').val(modifier)  
        $('.cp-attack-workspace__ability-scores-select--secondary').val(modifier)  
        $('.cp-attack-workspace__ability-scores-select--extra').val(modifier)  
    }
}

calcWorkspace('STR')

})
