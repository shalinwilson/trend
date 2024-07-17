/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

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
                if (elementId !== undefined){
                    console.log(this, "ffffffffffff");
                    $.ajax({
                        type: "POST",
                        dataType: 'json',
                        url: '/bidding/line/create',
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'po_id': elementId, 'price': bidding_price}}),
                        success: function(action){
                           console.log("result", action.result);
                        }
                    })
                }
                // Perform any additional logic needed with the elementId
            });
        }
});
