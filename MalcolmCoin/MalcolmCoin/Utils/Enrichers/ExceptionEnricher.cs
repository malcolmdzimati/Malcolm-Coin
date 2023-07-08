using Serilog.Core;
using Serilog.Events;

namespace malcolmcoin.Utils.Enrichers
{
    public class ExceptionEnricher : ILogEventEnricher
    {
        public void Enrich(LogEvent logEvent, ILogEventPropertyFactory propertyFactory)
        {
            if (logEvent.Exception == null)
                return;

            var logEventProperty = propertyFactory.CreateProperty(
                "EscapedException",
                logEvent.Exception.ToString().Replace("\r\n", "0x0A0D").Replace("\r", "0x0A").Replace("\n", "0x0D"));
            logEvent.AddPropertyIfAbsent(logEventProperty);
        }
    }
}
