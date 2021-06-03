module.exports = {
  apps: [
    {
      name: "OSSmosis: Django Server",
      interpreter: "python3",
      cwd: "server",
      script: "manage.py",
      args: "runserver",
    },
    {
      name: "OSSmosis: Vue Server",
      cwd: "web",
      script: "yarn",
      args: "serve",
    },
  ],
};
