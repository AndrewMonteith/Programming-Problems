using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace AdventOfCode
{

    class FirewallLayer
    {
        private int direction = 1;

        internal int Layer { get; }
        internal int Depth { get; private set; }
        internal int Position { get; private set; } = 1;

        internal void MoveScanner()
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

        internal void Simulate(int n)
        {
            n %= 2*(Depth - 1);

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

        private static bool DoPass(List<FirewallLayer> firewall, Func<FirewallLayer, bool> whenHit)
        {
            int maxDepth = firewall.Max(layer => layer.Layer);

            for (var position = 0; position <= maxDepth; position++)
            {
                var layer = firewall.FirstOrDefault(l => l.Layer == position);

                if (layer?.Position == 1)
                {
                    if (whenHit(layer)) // returns true if we should stop.
                        return false;
                }

                moveForward();
            }

            return true;

            void moveForward() => firewall.ForEach(layer => layer.MoveScanner()); ;
        }

        static int SeverityFor(string input)
        {
            var firewall = ParseInput("input.txt");
            int maxDepth = firewall.Max(layer => layer.Layer);

            int totalSeverity = 0;

            DoPass(firewall, layer =>
            {
                totalSeverity += (layer.Depth * layer.Layer);
                return false;
            });

            return totalSeverity;
        }

        static int CheckForDelay(string input)
        {
            var firewall = ParseInput("input.txt");
            
            var delay = 0;
            
            while (true)
            {
                firewall.ForEach(l => {
                    l.Reset();
                    l.Simulate(delay);
                });

                bool success = DoPass(firewall, _ => true);

                if (success)
                    return delay;
                else
                    delay += 1;
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine($"Calculated Severity {SeverityFor("input.txt")}");
            Console.WriteLine($"Delay required {CheckForDelay("input.txt")}");
            Console.Read();
        }
    }
}
