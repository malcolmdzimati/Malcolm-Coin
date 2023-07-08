using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;

namespace malcolmcoin.Controllers
{
    /// <inheritdoc />
    [ApiController]
    [ApiVersion("1")]
    [Route("[controller]/v{version:apiVersion}/sample")]
    public class SampleController : ControllerBase
    {
        /// <summary>
        /// Get all samples for the account number
        /// </summary>
        /// <param name="accountNumber"/>
        [HttpGet]
        [ProducesResponseType(typeof(string), 200)]
        public string GetSamples([FromRoute, Required] string accountNumber)
        {
            return string.Empty;
        }
    }
}
