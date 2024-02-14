// Executar quando o documento HTML for completamente carregado
document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  
  var calendar = new FullCalendar.Calendar(calendarEl, {
      locale: 'pt-br',
      themeSystem: 'bootstrap5',
      headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'multiMonthYear,dayGridMonth,timeGridWeek,timeGridDay'
      },
      initialDate: '2024-01-12',
      navLinks: true, // permite navegar clicando nos dias/semanas
      selectable: true,
      selectMirror: true,
      events: '/all_events', // URL para buscar eventos
      editable: true,
      select: function(info) {
          var title = prompt("Nome do Evento:");
          if (title) {
              var eventData = {
                  title: title,
                  start: info.startStr,
                  end: info.endStr,
              };
              // Chama a função para adicionar evento aqui
              addEvent(eventData);
          }
          calendar.unselect();
      },
      eventClick: function(info) {
          // Implemente a lógica de clique em evento aqui, se necessário
      },
      // Adicione outros manipuladores de eventos conforme necessário
  });

  calendar.render();

  function addEvent(eventData) {
      fetch('/add_event', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCsrfToken(), // Função para obter o token CSRF
          },
          body: JSON.stringify(eventData)
      })
      .then(response => response.json())
      .then(data => {
          if(data.status === "success") {
              calendar.refetchEvents();
              alert("Evento adicionado com sucesso");
          }
      })
      .catch(error => {
          console.error('Erro:', error);
          alert("Erro ao adicionar evento");
      });
  }

  function getCsrfToken() {
      // Retorna o valor do cookie CSRFToken do Django
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          if (cookie.startsWith('csrftoken=')) {
              return cookie.substring('csrftoken='.length, cookie.length);
          }
      }
    return '';
  }
  
});


// document.addEventListener('DOMContentLoaded', function() {
//   var calendarEl = document.getElementById('calendar');

//   var calendar = new FullCalendar.Calendar(calendarEl, {
//     locale: 'pt-br',
//     headerToolbar: {
//       left: 'prev,next today',
//       center: 'title',
//       right: 'multiMonthYear,dayGridMonth,timeGridWeek,timeGridDay'
//     },
//     initialDate: '2024-01-12',
//     navLinks: true, // can click day/week names to navigate views
//     selectable: true,
//     selectMirror: true,
//     events: '/all_events',
//     editable: true,
//     fetch('/add_event', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//         // Incluir o token CSRF aqui
//       },
//       body: JSON.stringify({title, start: start.format("YYYY-MM-DD HH:mm:ss"), end: end.format("YYYY-MM-DD HH:mm:ss")})
//     })
//     .then(response => response.json())
//     .then(data => {
//       if(data.status === "success") {
//         calendar.refetchEvents();
//         alert("Adicionado com sucesso");
//       }
//     })
//     .catch(error => {
//       console.error('Erro:', error);
//     });
//   });
// });
//     select: function (start, end, allDay) {
//       var title = prompt("Evento:");
//       if (title) {
//         var start = moment(start).format(start, "Y-MM-DD HH:mm:ss");
//         var end = moment(end).format(end, "Y-MM-DD HH:mm:ss");
//         fetch('/add_event', {
//           method: 'GET',
//           headers: { 'Content-Type': 'application/json' },
//           body: JSON.stringify({title, start: start, end: end })
//         })
//         // .then(response => response.json())
//         .then(data => {
//           calendar.refetchEvents();
//           alert("Adicionado com sucesso");
//         })
//         .catch(error => {
//           console.error(error);
//           alert('There is a problem!!!');
//         });
//         }
//     },
//     eventResize: function (event) {
//       var start = $.fullCalendar.formatDate(event.start, "Y-MM-DD HH:mm:ss");
//       var end = $.fullCalendar.formatDate(event.end, "Y-MM-DD HH:mm:ss");
//       var title = event.title;
//       var id = event.id;
//       $.ajax({
//           type: "GET",
//           url: '/update',
//           data: {'title': title, 'start': start, 'end': end, 'id': id},
//           dataType: "json",
//           success: function (data) {
//             calendar.fullCalendar('refetchEvents');
//             alert('Event Update');
//           },
//           error: function (data) {
//             alert('There is a problem!!!');
//           }
//       });
//     },
//     eventDrop: function (event) {
//       var start = $.fullCalendar.formatDate(event.start, "Y-MM-DD HH:mm:ss");
//       var end = $.fullCalendar.formatDate(event.end, "Y-MM-DD HH:mm:ss");
//       var title = event.title;
//       var id = event.id;
//       $.ajax({
//         type: "GET",
//         url: '/update',
//         data: {'title': title, 'start': start, 'end': end, 'id': id},
//         dataType: "json",
//         success: function (data) {
//           calendar.fullCalendar('refetchEvents');
//           alert('Event Update');
//         },
//         error: function (data) {
//           alert('There is a problem!!!');
//         }
//       });
//     },
//     eventClick: function (event) {
//       if (confirm("Are you sure you want to remove it?")) {
//         var id = event.id;
//           $.ajax({
//             type: "GET",
//             url: '/remove',
//             data: {'id': id},
//             dataType: "json",
//             success: function (data) {
//               calendar.fullCalendar('refetchEvents');
//              alert('Evento removido');
//             },
//             error: function (data) {
//               alert('Erro em remover!!!');
//             }
//           });
//         }
//       },
//     });
//   calendar.render();
// });