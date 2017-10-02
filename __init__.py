import jenkins
import logging

from opsdroid.matchers import match_regex

_LOGGER = logging.getLogger(__name__)


class JenkinsBot:
    def __init__(self, config, **kwargs):

        self.job = kwargs.get('job_name')

        try:
            username = config['credentials']['username']
            password = config['credentials']['password']
            url = config['jenkins_url']
        except FileNotFoundError:
            _LOGGER.error('jenkins_credentials.yaml not found. Please copy from template in '
                          'config/jenkins_credentials.yaml.example')

        self.server = jenkins.Jenkins(url, username=username, password=password)

    def build_job(self):

        # get list of jobs
        jobs = self.server.get_jobs(5)
        matches = []

        # scrape list of jobs for matches. append to list
        for i in jobs:
            job_path = i['fullname']
            # TODO if match -> matches.append(job_path)

        # TODO if matches only has one match:
        if():
            try:
                self.server.build_job(matches[0])
                return matches[0]
            except jenkins.NotFoundException:
                _LOGGER.info('job name {} found but path {} is incorrect'.format(self.job, job_path))
        # TODO else matches > 1:
        else:
            return matches
            # TODO return the list for user selelection


@match_regex(r"build (?P<job>\w+)", case_sensitive=False)
async def build_job(opsdroid, config, message):
    res = JenkinsBot.build_job(message.regex.group('job'))
    await message.respond('Job building..')
