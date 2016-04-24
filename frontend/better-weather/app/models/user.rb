class User < ActiveRecord::Base

  def self.create_with_omniauth(auth)
    create! do |user|
      user.provider = auth['provider']
      user.uid = auth['uid']
      puts '_______auth:'
      puts auth['info']
      if auth['info']
         user.name = auth['info']['name'] || ""
      end
    end
  end

end