# Opsdroid-Jenkins Skill

This provides the ability to interact with jenkins build jobs via an opsdroid connector of your choice.

##Configuration

Add the following skill configuration to the main opsdroid config. If using docker-compose, jenkins home is mounted to `~/.jenkins_home`.

**Note:** The `!include` separates out credentials so you can check your main configuration into source control

```
skills:
 - name: opsdroid-jenkins
   path: modules/opsdroid-jenkins
   credentials: !include jenkins_credentials.yamls
   jenkins_url: 'http://jenkins:8080'
```