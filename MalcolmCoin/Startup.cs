using InvCores.Middleware.Core;
using InvCores.Middleware.GlobalExceptionHandler;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System.Collections.Generic;

namespace malcolmcoin
{
    public class Startup
    {
        private readonly string _title = "$projectname$";
        private readonly string _description = "$projectname$";
        private readonly List<int> _versions = new List<int>() { 1 };
        private readonly InvCoresServicesOptions _invCoresServicesOptions = new InvCoresServicesOptions();
        private readonly IConfiguration _configuration;

        public Startup(IConfiguration configuration)
        {
            this._configuration = configuration;
        }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            var roles = new List<string>()
            {
            };

            services.ConfigureInvCoresServices(this._configuration, this._title, this._description, this._versions,
                roles,
                options =>
                {
                    options.ProducesBadRequest();
                    options.ProducesInternalServerError();
                }, _invCoresServicesOptions);

            this.RegisterConfigurationOptions(services);
            this.RegisterProviders(services);
            this.RegisterRepositories(services);
            this.RegisterBusinessLogics(services);
        }

        /// <summary>
        /// This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        /// </summary>
        /// <param name="app"></param>
        public void Configure(IApplicationBuilder app)
        {
            app.ConfigureInvCores(this._title, this._versions);
        }

        private void RegisterConfigurationOptions(IServiceCollection services)
        {
        }

        private void RegisterBusinessLogics(IServiceCollection services)
        {
        }

        private void RegisterProviders(IServiceCollection services)
        {

        }

        private void RegisterRepositories(IServiceCollection services)
        {
        }
    }
}
