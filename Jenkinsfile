
  env.DOCKERHUB_USERNAME = 'rolo1820'

  node("docker-prod") {
    stage("Production") {
      try {
        // Create the service if it doesn't exist otherwise just update the image
        sh '''
          SERVICES=$(docker service ls --filter name=pythondocker --quiet | wc -l)
          if [[ "$SERVICES" -eq 0 ]]; then
            docker service create --name pythondocker --network mongo --network bridge --replicas 2 rolo1820/pythondocker
          else
            docker service update --image rolo1820/pythondocker pythondocker
          fi
          '''
      }catch(e) {
        sh "docker service update --rollback  pythondocker"
        error "Service update failed in production"
      }finally {
        sh "docker ps -aq | xargs docker rm || true"
      }
    }
  }
