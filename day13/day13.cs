using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.CompilerServices;

namespace AdventOfCode
{

    class FirewallLayer
    {
        private int direction = 1;

        internal int Layer { get; }
        internal int Depth { get; private set; }
        internal int Position { get; private set; } = 1;

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        public void MoveScanner()
        {
            Position += direction;

            if (Position == Depth)
                direction = -1;
            else if (Position == 1)
                direction = 1;
        }

        internal void Reset()
        {
            Position = 1;
            direction = 1;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        internal void Simulate(int n)
        {
            for (var i = 0; i < n; i++)
                MoveScanner();
        }

        public FirewallLayer(int layer, int depth)
        {
            Layer = layer;
            Depth = depth;
        }

        internal static FirewallLayer ParseLine(string line)
        {
            var split = line.Split(':');

            return new FirewallLayer(int.Parse(split[0].Trim())
                , int.Parse(split[1].Trim()));
        }
    }


    class Program
    {
        static List<FirewallLayer> ParseInput(string fileName) 
            => File.ReadAllLines(fileName).Select(FirewallLayer.ParseLine).ToList();

        static int SeverityFor(string input)
        {
            var firewall = ParseInput("input.txt");
            int maxDepth = firewall.Max(layer => layer.Layer);

            int totalSeverity = 0;

            for (var position = 0; position <= maxDepth; position++)
            {
                var layer = firewall.FirstOrDefault(l => l.Layer == position);

                if (layer?.Position == 1)
                    totalSeverity += (position * layer.Depth);

                firewall.ForEach(l => l.MoveScanner());
            }

            return totalSeverity;
        }

        static int CheckForDelay(string input)
        {
            var firewall = ParseInput("input.txt");

            var delay = 0;
            var maxDepth = firewall.Max(layer => layer.Layer);

            while (true)
            {
            failed_pass:
                firewall.ForEach(l => l.Reset());
                firewall.ForEach(l => l.Simulate(delay % (2*(l.Depth-1) )));
                
                for (var position = 0; position <= maxDepth; position++)
                {
                    var layer = firewall.FirstOrDefault(l => l.Layer == position);

                    if (layer?.Position == 1)
                    {
                        delay += 1;
                        goto failed_pass;
                    }

                    moveForward();
                }

                return delay;
            }

            void moveForward() => firewall.ForEach(l => l.MoveScanner());
        }

        static void Main(string[] args)
        {
            Console.WriteLine($"Calculated Severity {SeverityFor("input.txt")}");
            Console.WriteLine($"Delay required {CheckForDelay("input.txt")}");
            Console.Read();
        }
    }
}
