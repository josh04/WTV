// Drag and drop ordering of admin list elements
// Combines code from http://djangosnippets.org/snippets/2306/
// and from http://djangosnippets.org/snippets/2057/
// to work both with and without admin-grappelli
//
// The model needs to have a field holding the position and that field has to 
// be made list_editable in the ModelAdmin. The changes of the ordering are 
// applied after clicking 'Save'.

(function($) {
    $(document).ready(function($) {
        if($('#result_list').length == 1)         // Grappelli not installed
            table = $('#result_list')[0];
        else if($('.changelist-results').length == 1) // Grappelli installed
            table = $('.changelist-results')[0];
        else {                                         // Unrecognized admin
            console.info("No sortable table found in the view, exiting");
            return;
        }
    
        // Set this to the name of the column holding the position
        pos_field = 'position';
    
        // Determine the column number of the position field
        pos_col = null;
        cols = $(table).find('tbody tr:first').children();
        for (i = 0; i < cols.length; i++) {
            inputs = $(cols[i]).find('input[name*=' + pos_field + ']');
            if (inputs.length > 0) {pos_col = i; break;}} // Found
        if (pos_col === null) return;                      // Not found
            
        // Some visual enhancements
        header = $(table).find('thead tr').children()[pos_col];
        $(header).css('width', '1em');
        $(header).children('a').text('#');
    
        // Hide position field
        $(table).find('tbody tr').each(function(index) {
            pos_td = $(this).children()[pos_col];
            input = $(pos_td).children('input').first();
            input.hide();
    
            label = $('<strong>' + input.attr('value') + '</strong>');
            $(pos_td).append(label);
        });
    
        // Determine sorted column and order
        sorted = $(table).find('thead th.sorted');
        sorted_col = $(table).find('thead th').index(sorted);
        sort_order = sorted.hasClass('descending') ? 'desc' : 'asc';
    
        if (sorted_col != pos_col) {
            // Sorted column is not position column, bail out
            console.info("Sorted column is not %s, bailing out", pos_field);
            return;
        }
    
        $(table).find('tbody tr').css('cursor', 'move');
    
        // Make tbody > tr sortable
        $(table).find('tbody').sortable({
            items: 'tr',
            cursor: 'move',
            update: function(event, ui) {
                item = ui.item;
                items = $(this).find('tr').get();
    
                if (sort_order == 'desc') {
                    // Reverse order
                    items.reverse();
                }
    
                $(items).each(function(index) {
                    pos_td = $(this).children()[pos_col];
                    input = $(pos_td).children('input').first();
                    label = $(pos_td).children('strong').first();
    
                    input.attr('value', index);
                    label.text(index);
                });
    
                // Update row classes
                $(this).find('tr').removeClass('row1').removeClass('row2');
                $(this).find('tr:even').addClass('row1');
                $(this).find('tr:odd').addClass('row2');
            }
        });
    });
})(jQuery);
