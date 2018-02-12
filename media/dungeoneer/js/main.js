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
        $('.cp-ability-count__toggle').text($('.ability').length)
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
    $('.cp-ability-count__toggle').text($('.ability:not(.hide)').length)
}    

// add a border to clicked elements
$('.ability').on('click', function() {
    $(this).toggleClass('clicked')
})

// show/hide dropdowns on click
$('.cp-ability-controls__dropdown legend').on('click', function() {
    if ($(this).parent().parent().hasClass('active')) {
        $('.cp-ability-controls__dropdown').removeClass('active')
    } else {
        $('.cp-ability-controls__dropdown').removeClass('active')
        $(this).parent().parent().addClass('active')
    }
})
})
