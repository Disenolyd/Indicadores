document.addEventListener('DOMContentLoaded', function () {
    console.log('Aplicación iniciando...');

    // Manejo del menú principal
    document.querySelectorAll('.menu > li > button').forEach(menuBtn => {
        menuBtn.addEventListener('click', function () {
            document.querySelectorAll('.menu > li > button').forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            document.querySelectorAll('.submenu').forEach(sub => sub.classList.remove('active'));

            const submenu = this.parentElement.querySelector('.submenu');
            if (submenu) {
                submenu.classList.add('active');

                const firstSubBtn = submenu.querySelector('button[data-submenu-id]');
                if (firstSubBtn) firstSubBtn.click(); // dispara showSection
            }
        });
    });

    // Delegación para submenús
    document.querySelectorAll('.submenu').forEach(submenu => {
        submenu.addEventListener('click', function (e) {
            const btn = e.target.closest('button[data-submenu-id]');
            if (btn) {
                showSection(btn.dataset.submenuId);
            }
        });
    });

    // Botones de PDF
    document.querySelectorAll('.btn-pdf').forEach(btn => {
        btn.addEventListener('click', function () {
            const submenu = this.dataset.submenu;
            const periodicidad = this.dataset.periodicidad;
            if (submenu && periodicidad) {
                descargarPDF(submenu, periodicidad);
            }
        });
    });
});

// Mostrar sección de indicadores
function showSection(submenuId) {
    console.log("Sección activada:", submenuId);

    document.querySelectorAll('.section-content').forEach(sec => {
        sec.style.display = 'none';
    });

    const section = document.getElementById('section-' + submenuId);
    if (section) section.style.display = 'block';

    // Título principal
    const titulo = section?.querySelector('h3')?.textContent || 'Indicador';
    document.getElementById('tituloSubmenu').textContent = titulo;

    // Activar botón correspondiente
    document.querySelectorAll('.submenu button').forEach(btn => btn.classList.remove('activo'));
    const activeBtn = document.querySelector(`.submenu button[data-submenu-id="${submenuId}"]`);
    if (activeBtn) activeBtn.classList.add('activo');

    // Mostrar botones según periodicidad
    mostrarBotonesReporte(submenuId);

    // Cargar reporte por defecto
    mostrarReporteAnual(submenuId);

    window.submenuActual = submenuId;
}

// Exportar PDF
function descargarPDF(submenu, periodicidad) {
    const section = document.getElementById('section-' + submenu);
    if (!section) return;

    const opt = {
        margin: 10,
        filename: `reporte-${submenu}-${periodicidad}.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'landscape' }
    };
    html2pdf().set(opt).from(section).save();
}
