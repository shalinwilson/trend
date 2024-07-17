/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.PurchasePortal = publicWidget.Widget.extend({
     selector: '#bidding_portal',
        events: {
            'click #bidding_update': '_update_po_lines',
        },
         init: function () {
            this._super.apply(this, arguments);
        },
        _update_po_lines: function(){
            var self = this;
            console.log("aaaaaaaaaaaaaaaaa", this);
            var bidding_price = $("#bidding_price").val();
            console.log("bidding price", bidding_price);
            var url = window.location.pathname;  // Get the path from the URL
            var parts = url.split('/');  // Split the path by '/'
            var id = parts.pop() || parts.pop();
            console.log("id", id);
            var hiddenInputs = $('input[type="hidden"]');
            hiddenInputs.each(function() {
                var elementId = $(this).attr('id');
                console.log(elementId);
                // Perform any additional logic needed with the elementId
            });
        }
});
