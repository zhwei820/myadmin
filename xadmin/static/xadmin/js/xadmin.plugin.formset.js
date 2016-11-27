;(function($) {
    $.fn.formset = function(opts){
        var $$ = $(this);

        // var 
        options = $.extend({
            prefix: $$.data('prefix')
        }, $.fn.formset.styles[$$.data('style')], opts),

            updateElementIndex = function(elem, prefix, ndx) {
                var idRegex = new RegExp(prefix + '-(\\d+|__prefix__)-'),
                    replacement = prefix + '-' + ndx + '-';
                if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
                if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
                if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
                if (elem.attr('href')) elem.attr('href', elem.attr('href').replace(idRegex, replacement));
                elem.find('.formset-num').html(ndx + 1);
            },

            hasChildElements = function(row) {
                return row.find('input,select,textarea,label,div,a').length > 0;
            },

            updateRowIndex = function(row, i){
                if (options.update) options.update(row, (function(elem){
                    updateElementIndex(elem, options.prefix, i);
                }));
                updateElementIndex(row, options.prefix, i);
                row.find('input,select,textarea,label,div,a').each(function() {
                    updateElementIndex($(this), options.prefix, i);
                });
                row.data('row-index', i);
            },

            insertDeleteLink = function(row) {
                row.find('a.delete-row').click(function() {
                    var row = $(this).parents(".formset-row"),
                        del = row.find('input[id $= "-DELETE"]');

                    if (options.removed) options.removed(row, del, $$);

                    if (del.length) {
                        if(del.val() == 'on'){
                            row.removeClass('row-deleted');
                        } else {
                            row.addClass('row-deleted');
                        }
                        del.val(del.val() == 'on'?'':'on');
                    } else {
                        var parent = row.parent();
                        row.remove();
                        var forms = parent.find('.formset-row');
                        $('#id_' + options.prefix + '-TOTAL_FORMS').val(forms.length);
                        for (var i=0, formCount=forms.length; i<formCount; i++) {
                            updateRowIndex(forms.eq(i), i);
                        }
                    }
                    return false;
                });
            };

        $$.find(".formset-row").each(function(i) {
            insertDeleteLink($(this));
        });

        if ($$.length) {
            var template, el = $('#' + options.prefix + '-empty');
            if(el.is('textarea')) {
                template = el.val();
            } else if(el.is('span')) {
                template = el.html();
            }else if(el.is('script')) {
                template = el.html();
            }

            template = el.html(template).text(); // decoded
            template = $($.parseHTML(template));

            template.removeAttr('id');
            if(template.data("replace-id")){
                template.attr('id', template.data("replace-id"));
                template.removeAttr('data-replace-id');
            }
            options.formTemplate = template;

            $('#' + options.prefix + '-add-row').click(function() {
                var formCount = parseInt($('#id_' + options.prefix + '-TOTAL_FORMS').val()),
                    row = options.formTemplate.clone(true).removeClass('empty-form');
                updateRowIndex(row, formCount);
                row.appendTo($$);
                insertDeleteLink(row);
                row.exform();
                $('#id_' + options.prefix + '-TOTAL_FORMS').val(formCount + 1);
                // If a post-add callback was supplied, call it with the added form:
                if (options.added) options.added(row, $$);
                return false;
            });

////////////////////////////////////////

            $("#generate_cron").click(function(){
                var r = $(".formset-row")
                for(var ii = 0; ii < r.length; ii++){
                    if(!$(r[ii]).hasClass("row-delete")){
                        var cc = $(r[ii]).addClass("row-deleted")
                    }
                }

                var id_start_time_0 = Date.parse($("#id_start_time_0").val())
                var id_start_time_1 = $("#id_start_time_1").val()

                var id_end_time_0 = Date.parse($("#id_end_time_0").val())
                var id_end_time_1 = $("#id_end_time_1").val()

                var id_cpm_num_all = $("#id_cpm_num_all").val()
                var id_cpc_num_all = $("#id_cpc_num_all").val()

                render_cron(id_start_time_0, id_end_time_0, id_start_time_1, id_end_time_1, id_cpm_num_all, id_cpc_num_all)
                return false;                
            })
/////////////////////////////////////////////

        }

        return $$;
    }

/////////////////////////////////////////////
        function render_cron(start_date, end_date, start_hour, end_hour, cpm_num_all, cpc_num_all){  // 
            var kk = 0;
            var now = new Date();
            var days = parseInt((end_date - start_date) / (3600 * 24 * 1000)) + 1;

            for(var ii = start_date; ii < end_date; ii += 3600 * 24 * 1000){
                $("#timeintervals_set-add-row").click()
            }
            for(var ii = start_date; ii <= end_date; ii += 3600 * 24 * 1000){
                $("#id_timeintervals_set-" + kk + "-start_time_0").val((new Date(ii)).Format("yyyy-MM-dd"))
                $("#id_timeintervals_set-" + kk + "-start_time_1").val(start_hour)
                $("#id_timeintervals_set-" + kk + "-end_time_0").val((new Date(ii)).Format("yyyy-MM-dd"))
                $("#id_timeintervals_set-" + kk + "-end_time_1").val(end_hour)
                $("#id_timeintervals_set-" + kk + "-cpm_num1").val(parseInt(cpm_num_all / days))
                $("#id_timeintervals_set-" + kk + "-cpc_num1").val(parseInt(cpc_num_all / days))
                kk ++
            }
        }
/////////////////////////////////////////////

    $.fn.formset.styles = {
        'tab': {
            added: function(row, $$){
                var new_tab = $('<li><a data-toggle="tab" href="#'+ row.attr('id') +'">#<span class="formset-num">'+ (row.data('row-index') + 1) +'</span></a></li>');
                $$.parent().find('.nav-tabs').append(new_tab);
                new_tab.find('a').tab('show');
            },
            update: function(row, update){
                var rowId = row.attr('id');
                if(rowId){
                    $('a[href=#'+rowId+']').each(function(){
                        update($(this));
                    })
                }
            },
            removed: function(row, del, $$){
                var rowId = row.attr('id');
                if(rowId){
                    var tab = $('a[href=#'+rowId+']');
                    if (del.length) {
                        if(del.val() == 'on'){
                            tab.removeClass('row-deleted');
                        } else {
                            tab.addClass('row-deleted');
                        }
                    } else {
                        if(tab.parent().next().length){
                            tab.parent().next().find('a').tab('show');
                        } else {
                            tab.parent().prev().find('a').tab('show');
                        }
                        tab.parent().remove();
                    }
                }
            }
        }
    };

    $(function(){
        $('.formset-content').each(function(){
            $(this).formset();
        });
    });


// custom   //////////////////////////

    var a = $("#div_id_end_time")
    if(a){
        var name = $("#id_name").val()
        if(!name){
            var s = '<div class="form-group"><label class="control-label">aaaa</label><div class="controls">\
            <input type="button" class="btn btn-primary" id="generate_cron" value="生成">\
            </div></div>'
            a.addClass("inline-block")
            a.append(s)
        }
    }
////////////////////////////////

})(jQuery);
