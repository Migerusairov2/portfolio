 const logos = [
    { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg", alt: "React" },
    { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", alt: "Python" },
    { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg", alt: "Django" },
    { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", alt: "JavaScript" },
    { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg", alt: "Node" },
    { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg", alt: "PostgreSQL" }
  ];

  const track = document.getElementById("logo-track");

  // Repeat logos multiple times for marquee effect
  const repeatCount = 99;
  for (let i = 0; i < repeatCount; i++) {
    logos.forEach(logo => {
      const img = document.createElement("img");
      img.src = logo.src;
      img.alt = logo.alt;
      track.appendChild(img);
    });
  }