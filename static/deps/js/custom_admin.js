// custom_admin.js

(function($) {
    $(document).ready(function() {
        // Функция, которая скрывает или отображает поля в зависимости от выбранной категории товара
        function toggleFields() {
            // Получаем выбранную категорию
            var selectedCategory = $('#id_category').find(':selected').text().toLowerCase();
            // Скрываем все поля
            $('.field-technology, .field-resolution, .field-print_speed, .field-trays, .field-connection, .field-dopf, .field-interf, .field-dlay, .field-typef, .field-color, .field-form, .field-pocr, .field-plotn, .field-collist').hide();
            
            // В зависимости от выбранной категории показываем соответствующие поля
            if (selectedCategory === 'принтеры') {
                $('.field-technology, .field-resolution, .field-print_speed, .field-trays, .field-connection').show();
            } else if (selectedCategory === 'мфу') {
                $('.field-technology, .field-resolution, .field-print_speed, .field-trays, .field-connection, .field-dopf').show();
            } else if (selectedCategory === 'сканеры') {
                $('.field-technology, .field-resolution, .field-print_speed, .field-trays, .field-connection, .field-interf').show();
            } else if (selectedCategory === 'тонеры') {
                $('.field-dlay, .field-typef, .field-color').show();
            } else if (selectedCategory === 'картриджи') {
                $('.field-dlay, .field-resurs, .field-color').show();
            } else if (selectedCategory === 'бумага') {
                $('.field-form, .field-pocr, .field-plotn, .field-collist').show();
            }
        }

        // Вызываем функцию при загрузке страницы и каждый раз, когда меняется выбранная категория товара
        toggleFields();
        $('#id_category').change(toggleFields);
    });
})(django.jQuery);