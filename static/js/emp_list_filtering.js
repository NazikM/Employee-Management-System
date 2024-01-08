$(document).ready(function() {
  $('#filter-form').on('submit', function(event) {
    event.preventDefault();
    filterEmployees();
  });

  function filterEmployees() {
    const formData = $('#filter-form').serialize();
    $.ajax({
      url: window.location.href,
      type: 'GET',
      data: formData,
      success: function(data) {
        $('#employee-table tbody').html(data.html);
      },
      error: function(error) {
        console.error('Error:', error);
      }
    });
  }

  // Sorting logic
  $('#employee-table th').on('click', function() {
    const sortField = $(this).data('sort-field');
    $('#sort_field').val(sortField);
    filterEmployees();
  });
});